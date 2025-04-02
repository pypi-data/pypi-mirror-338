"""Custom exceptions for the ybl-mcp server."""


class YblMcpError(Exception):
    """Base exception for all ybl-mcp errors."""

    pass


class ResourceNotFoundError(YblMcpError):
    """Raised when a requested resource is not found."""

    pass


class ResourceAccessError(YblMcpError):
    """Raised when there's an error accessing a resource."""

    pass


class InvalidArgumentError(YblMcpError):
    """Raised when an invalid argument is provided."""

    pass


class ToolExecutionError(YblMcpError):
    """Raised when there's an error executing a tool."""

    pass


class PromptGenerationError(YblMcpError):
    """Raised when there's an error generating a prompt."""

    pass


class DuplicateResourceError(YblMcpError):
    """Raised when attempting to create a resource that already exists."""

    pass
