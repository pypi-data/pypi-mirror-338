"""Base resource provider interfaces."""

from abc import ABC, abstractmethod

from mcp import types
from pydantic import AnyUrl


class ResourceProvider(ABC):
    """Abstract base class for resource providers."""

    @abstractmethod
    async def list_resources(self) -> list[types.Resource]:
        """
        List resources provided by this provider.

        Returns:
            List of Resource objects
        """
        pass

    @abstractmethod
    async def read_resource(self, uri: AnyUrl) -> str:
        """
        Read a resource by URI.

        Args:
            uri: The URI of the resource to read

        Returns:
            The resource content as a string

        Raises:
            ResourceNotFoundError: If the resource is not found
            ResourceAccessError: If there's an error accessing the resource
        """
        pass
