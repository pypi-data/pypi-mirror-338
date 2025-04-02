# src/ybl_mcp/registry.py
from .prompts.base import PromptProvider
from .resources.base import ResourceProvider
from .tools.base import ToolProvider


class ProviderRegistry:
    """Registry for all providers in the system."""

    def __init__(self):
        self._resource_providers: list[ResourceProvider] = []
        self._prompt_providers: list[PromptProvider] = []
        self._tool_providers: list[ToolProvider] = []

    def register_resource_provider(self, provider: ResourceProvider) -> None:
        """Register a resource provider."""
        self._resource_providers.append(provider)

    def register_prompt_provider(self, provider: PromptProvider) -> None:
        """Register a prompt provider."""
        self._prompt_providers.append(provider)

    def register_tool_provider(self, provider: ToolProvider) -> None:
        """Register a tool provider."""
        self._tool_providers.append(provider)

    @property
    def resource_providers(self) -> list[ResourceProvider]:
        """Get all registered resource providers."""
        return self._resource_providers

    @property
    def prompt_providers(self) -> list[PromptProvider]:
        """Get all registered prompt providers."""
        return self._prompt_providers

    @property
    def tool_providers(self) -> list[ToolProvider]:
        """Get all registered tool providers."""
        return self._tool_providers


# Global registry instance
registry = ProviderRegistry()
