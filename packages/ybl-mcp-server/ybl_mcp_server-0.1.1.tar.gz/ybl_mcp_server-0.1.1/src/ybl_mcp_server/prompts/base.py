"""Base prompt provider interfaces."""

from abc import ABC, abstractmethod

from mcp import types


class PromptProvider(ABC):
    """Abstract base class for prompt providers."""

    @abstractmethod
    async def list_prompts(self) -> list[types.Prompt]:
        """
        List prompts provided by this provider.

        Returns:
            List of Prompt objects
        """
        pass

    @abstractmethod
    async def get_prompt(
        self, name: str, arguments: dict[str, str]
    ) -> types.GetPromptResult:
        """
        Get a prompt by name with arguments.

        Args:
            name: The name of the prompt
            arguments: Dictionary of prompt arguments

        Returns:
            GetPromptResult containing the generated prompt

        Raises:
            PromptGenerationError: If there's an error generating the prompt
            InvalidArgumentError: If invalid arguments are provided
        """
        pass
