"""Base tool provider interfaces."""

from abc import ABC, abstractmethod

from mcp import types
from mcp.server import Server


class ToolProvider(ABC):
    """Abstract base class for tool providers."""

    @abstractmethod
    async def list_tools(self) -> list[types.Tool]:
        """
        List tools provided by this provider.

        Returns:
            List of Tool objects
        """
        pass

    @abstractmethod
    async def call_tool(
        self, name: str, arguments: dict, server: Server
    ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        """
        Call a tool by name with arguments.

        Args:
            name: The name of the tool
            arguments: Dictionary of tool arguments
            server: The MCP server instance

        Returns:
            List of content objects representing the tool's output

        Raises:
            ToolExecutionError: If there's an error executing the tool
            InvalidArgumentError: If invalid arguments are provided
        """
        pass
