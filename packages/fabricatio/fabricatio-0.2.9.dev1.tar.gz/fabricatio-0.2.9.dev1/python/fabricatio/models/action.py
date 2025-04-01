"""Module that contains the classes for actions and workflows.

This module defines the Action and WorkFlow classes, which are used for
creating and executing sequences of actions in a task-based context.
"""

import traceback
from abc import abstractmethod
from asyncio import Queue, create_task
from typing import Any, Dict, Self, Tuple, Type, Union, final

from fabricatio.journal import logger
from fabricatio.models.generic import WithBriefing
from fabricatio.models.task import Task
from fabricatio.models.usages import LLMUsage, ToolBoxUsage
from pydantic import Field, PrivateAttr

OUTPUT_KEY = "task_output"

INPUT_KEY = "task_input"


class Action(WithBriefing, LLMUsage):
    """Class that represents an action to be executed in a workflow.

    Actions are the atomic units of work in a workflow. Each action performs
    a specific operation and can modify the shared context data.
    """

    name: str = Field(default="")
    """The name of the action."""

    description: str = Field(default="")
    """The description of the action."""

    personality: str = Field(default="")
    """The personality traits or context for the action executor."""

    output_key: str = Field(default="")
    """The key used to store this action's output in the context dictionary."""

    @final
    def model_post_init(self, __context: Any) -> None:
        """Initialize the action by setting default name and description if not provided.

        Args:
            __context: The context to be used for initialization.
        """
        self.name = self.name or self.__class__.__name__
        self.description = self.description or self.__class__.__doc__ or ""

    @abstractmethod
    async def _execute(self, *_, **cxt) -> Any:  # noqa: ANN002
        """Execute the action logic with the provided context arguments.

        This method must be implemented by subclasses to define the actual behavior.

        Args:
            **cxt: The context dictionary containing input and output data.

        Returns:
            Any: The result of the action execution.
        """
        pass

    @final
    async def act(self, cxt: Dict[str, Any]) -> Dict[str, Any]:
        """Perform the action and update the context with results.

        Args:
            cxt: The context dictionary containing input and output data.

        Returns:
            Dict[str, Any]: The updated context dictionary.
        """
        ret = await self._execute(**cxt)

        if self.output_key:
            logger.debug(f"Setting output: {self.output_key}")
            cxt[self.output_key] = ret

        return cxt

    @property
    def briefing(self) -> str:
        """Return a formatted description of the action including personality context if available.

        Returns:
            str: Formatted briefing text with personality and action description.
        """
        if self.personality:
            return f"## Your personality: \n{self.personality}\n# The action you are going to perform: \n{super().briefing}"
        return f"# The action you are going to perform: \n{super().briefing}"

    def to_task_output(self)->Self:
        """Set the output key to OUTPUT_KEY and return the action instance."""
        self.output_key=OUTPUT_KEY
        return self

class WorkFlow(WithBriefing, ToolBoxUsage):
    """Class that represents a sequence of actions to be executed for a task.

    A workflow manages the execution of multiple actions in sequence, passing
    a shared context between them and handling task lifecycle events.
    """

    description: str = ""
    """The description of the workflow, which describes the workflow's purpose and requirements."""

    _context: Queue[Dict[str, Any]] = PrivateAttr(default_factory=lambda: Queue(maxsize=1))
    """Queue for storing the workflow execution context."""

    _instances: Tuple[Action, ...] = PrivateAttr(default_factory=tuple)
    """Instantiated action objects to be executed in this workflow."""

    steps: Tuple[Union[Type[Action], Action], ...] = Field(
        frozen=True,
    )
    """The sequence of actions to be executed, can be action classes or instances."""

    task_input_key: str = Field(default=INPUT_KEY)
    """Key used to store the input task in the context dictionary."""

    task_output_key: str = Field(default=OUTPUT_KEY)
    """Key used to extract the final result from the context dictionary."""

    extra_init_context: Dict[str, Any] = Field(default_factory=dict, frozen=True)
    """Additional initial context values to be included at workflow start."""

    def model_post_init(self, __context: Any) -> None:
        """Initialize the workflow by instantiating any action classes.

        Args:
            __context: The context to be used for initialization.
        """
        # Convert any action classes to instances
        self._instances = tuple(step if isinstance(step, Action) else step() for step in self.steps)

    def inject_personality(self, personality: str) -> Self:
        """Set the personality for all actions that don't have one defined.

        Args:
            personality: The personality text to inject.

        Returns:
            Self: The workflow instance for method chaining.
        """
        for action in filter(lambda a: not a.personality, self._instances):
            action.personality = personality
        return self

    async def serve(self, task: Task) -> None:
        """Execute the workflow to fulfill the given task.

        This method manages the complete lifecycle of processing a task through
        the workflow's sequence of actions.

        Args:
            task: The task to be processed.
        """
        logger.info(f"Start execute workflow: {self.name}")

        await task.start()
        await self._init_context(task)

        current_action = None
        try:
            # Process each action in sequence
            for step in self._instances:
                current_action = step.name
                logger.info(f"Executing step >> {current_action}")

                # Get current context and execute action
                context = await self._context.get()
                act_task = create_task(step.act(context))
                # Handle task cancellation
                if task.is_cancelled():
                    logger.warning(f"Task cancelled by task: {task.name}")
                    act_task.cancel(f"Cancelled by task: {task.name}")
                    break

                # Update context with modified values
                modified_ctx = await act_task
                logger.success(f"Step execution finished: {current_action}")
                if step.output_key:
                    logger.success(f"Setting output to `{step.output_key}`")
                await self._context.put(modified_ctx)

            logger.success(f"Workflow execution finished: {self.name}")

            # Get final context and extract result
            final_ctx = await self._context.get()
            result = final_ctx.get(self.task_output_key)

            if self.task_output_key not in final_ctx:
                logger.warning(
                    f"Task output key: `{self.task_output_key}` not found in the context, None will be returned. "
                    f"You can check if `Action.output_key` is set the same as `WorkFlow.task_output_key`."
                )

            await task.finish(result)

        except Exception as e:  # noqa: BLE001
            logger.critical(f"Error during task: {current_action} execution: {e}")
            logger.critical(traceback.format_exc())
            await task.fail()

    async def _init_context[T](self, task: Task[T]) -> None:
        """Initialize the context dictionary for workflow execution.

        Args:
            task: The task being served by this workflow.
        """
        logger.debug(f"Initializing context for workflow: {self.name}")
        initial_context = {self.task_input_key: task, **dict(self.extra_init_context)}
        await self._context.put(initial_context)

    def steps_fallback_to_self(self) -> Self:
        """Configure all steps to use this workflow's configuration as fallback.

        Returns:
            Self: The workflow instance for method chaining.
        """
        self.hold_to(self._instances)
        return self

    def steps_supply_tools_from_self(self) -> Self:
        """Provide this workflow's tools to all steps in the workflow.

        Returns:
            Self: The workflow instance for method chaining.
        """
        self.provide_tools_to(self._instances)
        return self

    def update_init_context(self, /, **kwargs) -> Self:
        """Update the initial context with additional key-value pairs.

        Args:
            **kwargs: Key-value pairs to add to the initial context.

        Returns:
            Self: The workflow instance for method chaining.
        """
        self.extra_init_context.update(kwargs)
        return self
