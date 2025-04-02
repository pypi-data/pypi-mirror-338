from mcp import types
from mcp.server.session import ServerSession

from ..models import NoteStore
from .base import ToolProvider


class NoteToolProvider(ToolProvider):
    """Provider for note-related tools."""

    def __init__(self, note_store: NoteStore):
        self.note_store = note_store

    async def list_tools(self) -> list[types.Tool]:
        """List available tools."""
        return [
            types.Tool(
                name="add-note",
                description="Add a new note",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "content": {"type": "string"},
                        "tags": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional tags for categorizing the note",
                        },
                    },
                    "required": ["name", "content"],
                },
            ),
            types.Tool(
                name="update-note",
                description="Update an existing note",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "content": {"type": "string"},
                    },
                    "required": ["name", "content"],
                },
            ),
            types.Tool(
                name="delete-note",
                description="Delete a note",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                    },
                    "required": ["name"],
                },
            ),
            types.Tool(
                name="search-notes",
                description="Search notes by keyword",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "keyword": {"type": "string"},
                    },
                    "required": ["keyword"],
                },
            ),
            types.Tool(
                name="tag-note",
                description="Add tags to a note",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["name", "tags"],
                },
            ),
        ]

    async def call_tool(
        self, name: str, arguments: dict, session: ServerSession
    ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        """Handle tool execution requests."""
        try:
            if name == "add-note":
                return await self._handle_add_note(arguments, session)
            elif name == "update-note":
                return await self._handle_update_note(arguments, session)
            elif name == "delete-note":
                return await self._handle_delete_note(arguments, session)
            elif name == "search-notes":
                return await self._handle_search_notes(arguments)
            elif name == "tag-note":
                return await self._handle_tag_note(arguments, session)
            else:
                raise ValueError(f"Unknown tool: {name}")
        except ValueError as e:
            return [types.TextContent(type="text", text=f"Error: {str(e)}")]

    async def _handle_add_note(
        self, arguments: dict, session: ServerSession
    ) -> list[types.TextContent]:
        """Handle adding a new note."""
        note_name = arguments.get("name")
        content = arguments.get("content")
        tags = arguments.get("tags", [])

        if not note_name or not content:
            raise ValueError("Missing name or content")

        # Add note to store
        note = self.note_store.add(note_name, content, tags)

        # Notify clients that resources have changed
        await session.send_resource_list_changed()

        return [
            types.TextContent(
                type="text",
                text=f"Added note '{note_name}' with content: {content}\n"
                f"Tags: {', '.join(note.tags) if note.tags else 'None'}",
            )
        ]

    async def _handle_update_note(
        self, arguments: dict, session: ServerSession
    ) -> list[types.TextContent]:
        """Handle updating an existing note."""
        note_name = arguments.get("name")
        content = arguments.get("content")

        if not note_name or not content:
            raise ValueError("Missing name or content")

        # Update note in store
        self.note_store.update(note_name, content)

        # Notify clients that resources have changed
        await session.send_resource_list_changed()

        return [
            types.TextContent(
                type="text", text=f"Updated note '{note_name}'\nNew content: {content}"
            )
        ]

    async def _handle_delete_note(
        self, arguments: dict, session: ServerSession
    ) -> list[types.TextContent]:
        """Handle deleting a note."""
        note_name = arguments.get("name")

        if not note_name:
            raise ValueError("Missing note name")

        # Delete note from store
        self.note_store.delete(note_name)

        # Notify clients that resources have changed
        await session.send_resource_list_changed()

        return [types.TextContent(type="text", text=f"Deleted note '{note_name}'")]

    async def _handle_search_notes(self, arguments: dict) -> list[types.TextContent]:
        """Handle searching notes."""
        keyword = arguments.get("keyword")

        if not keyword:
            raise ValueError("Missing keyword")

        # Search notes
        matching_notes = self.note_store.search(keyword)

        if not matching_notes:
            return [
                types.TextContent(
                    type="text", text=f"No notes found matching '{keyword}'"
                )
            ]

        result = f"Found {len(matching_notes)} notes matching '{keyword}':\n\n"
        for note in matching_notes:
            con = 100
            # Truncate content if too long
            content_preview = note.content[:con] + (
                "..." if len(note.content) > con else ""
            )
            result += f"- {note.name} (tags: {', '.join(note.tags) if note.tags else 'None'})\n  {content_preview}\n"

        return [types.TextContent(type="text", text=result)]

    async def _handle_tag_note(
        self, arguments: dict, session: ServerSession
    ) -> list[types.TextContent]:
        """Handle adding tags to a note."""
        note_name = arguments.get("name")
        tags = arguments.get("tags", [])

        if not note_name:
            raise ValueError("Missing note name")

        if not tags:
            raise ValueError("No tags provided")

        # Get note and add tags
        note = self.note_store.get(note_name)
        for tag in tags:
            note.add_tag(tag)

        # Notify clients that resources have changed
        await session.send_resource_list_changed()

        return [
            types.TextContent(
                type="text",
                text=f"Added tags to note '{note_name}'\nCurrent tags: {', '.join(note.tags)}",
            )
        ]
