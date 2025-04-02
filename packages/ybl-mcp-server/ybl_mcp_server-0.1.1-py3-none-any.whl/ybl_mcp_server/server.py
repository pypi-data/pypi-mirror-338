"""Main MCP server implementation."""

import asyncio

import mcp.server.stdio
from mcp import types
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from mcp.types import EmbeddedResource, ImageContent, TextContent
from pydantic import AnyUrl

from ybl_mcp_server.utils import logger

from .constants import MCP_SERVER_NAME, MCP_SERVER_VERSION
from .exceptions import ResourceAccessError, ResourceNotFoundError
from .models import NoteStore
from .prompts.note_prompts import NotePromptProvider
from .registry import registry
from .resources.notes import NoteResourceProvider
from .tools.note_tools import NoteToolProvider

# Initialize shared data store
note_store = NoteStore()

# Register providers in the registry
registry.register_resource_provider(NoteResourceProvider(note_store))
registry.register_prompt_provider(NotePromptProvider(note_store))
registry.register_tool_provider(NoteToolProvider(note_store))
# Create Server instance
server = Server(MCP_SERVER_NAME)


@server.list_resources()
async def handle_list_resources() -> list[types.Resource]:
    """
    List available resources.

    Returns:
        List of Resource objects
    """
    logger.debug("Handling list_resources request")
    all_resources = []
    for provider in registry.resource_providers:
        resources = await provider.list_resources()
        all_resources.extend(resources)
    return all_resources


@server.read_resource()
async def handle_read_resource(uri: AnyUrl) -> str:
    """
    Read a specific resource by its URI.

    Args:
        uri: The URI of the resource to read

    Returns:
        The resource content as a string

    Raises:
        ResourceNotFoundError: If the resource is not found
        ResourceAccessError: If there's an error accessing the resource
    """
    logger.debug(f"Handling read_resource request for URI: {uri}")
    # Try each provider until one succeeds
    for provider in registry.resource_providers:
        try:
            return await provider.read_resource(uri)
        except ResourceNotFoundError:
            # Try the next provider
            continue
        except ResourceAccessError as e:
            # If it's an access error, don't try other providers
            logger.error(f"Error accessing resource: {str(e)}")
            raise

    # If we get here, no provider could handle the resource
    error_msg = f"No provider could handle resource with URI: {uri}"
    logger.error(error_msg)
    raise ResourceNotFoundError(error_msg)


@server.list_prompts()
async def handle_list_prompts() -> list[types.Prompt]:
    """
    List available prompts.

    Returns:
        List of Prompt objects
    """
    logger.debug("Handling list_prompts request")
    all_prompts = []
    for provider in registry.prompt_providers:
        prompts = await provider.list_prompts()
        all_prompts.extend(prompts)
    return all_prompts


@server.get_prompt()
async def handle_get_prompt(
    name: str, arguments: dict[str, str] | None
) -> types.GetPromptResult:
    """
    Generate a prompt by name with arguments.

    Args:
        name: The name of the prompt
        arguments: Dictionary of prompt arguments

    Returns:
        GetPromptResult containing the generated prompt

    Raises:
        ValueError: If the prompt generation fails
    """
    logger.debug(f"Handling get_prompt request for prompt: {name}")

    # Try each provider until one succeeds
    errors = []
    for provider in registry.prompt_providers:
        try:
            return await provider.get_prompt(name, arguments or {})
        except Exception as e:
            # Record the error and try the next provider
            errors.append(str(e))
            continue

    # If we get here, no provider could handle the prompt
    error_msg = f"No provider could handle prompt '{name}'. Errors: {', '.join(errors)}"
    logger.error(error_msg)
    raise ValueError(error_msg)


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """
    List available tools.

    Returns:
        List of Tool objects
    """
    logger.debug("Handling list_tools request")
    all_tools = []
    for provider in registry.tool_providers:
        tools = await provider.list_tools()
        all_tools.extend(tools)
    return all_tools


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[TextContent | ImageContent | EmbeddedResource]:
    """
    Handle tool execution requests.

    Args:
        name: The name of the tool
        arguments: Dictionary of tool arguments

    Returns:
        List of content objects representing the tool's output
    """
    logger.debug(f"Handling call_tool request for tool: {name}")
    session = server.request_context.session

    # Try each provider until one succeeds
    for provider in registry.tool_providers:
        try:
            result = await provider.call_tool(name, arguments or {}, session)

            # Notify clients that resources might have changed
            await session.send_resource_list_changed()

            return result
        except ValueError:
            # This provider doesn't know this tool, try the next one
            continue
        except Exception as e:
            # An actual error occurred during execution
            logger.error(f"Error calling tool: {str(e)}")
            return [TextContent(type="text", text=f"Error: {str(e)}")]

    # If we get here, no provider recognized the tool
    error_msg = f"Unknown tool: {name}"
    logger.error(error_msg)
    return [TextContent(type="text", text=f"Error: {error_msg}")]


async def main():
    logger.info(f"Starting {MCP_SERVER_NAME} server")
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=MCP_SERVER_NAME,
                server_version=MCP_SERVER_VERSION,
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())
