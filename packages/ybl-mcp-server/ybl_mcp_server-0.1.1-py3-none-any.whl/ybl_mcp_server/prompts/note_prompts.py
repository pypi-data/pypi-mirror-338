"""Note prompt provider implementation."""

from mcp import types

from ybl_mcp_server.utils import logger

from ..exceptions import (
    InvalidArgumentError,
    PromptGenerationError,
    ResourceNotFoundError,
)
from ..models import NoteStore
from .base import PromptProvider


class NotePromptProvider(PromptProvider):
    """Provider for note-related prompts."""

    def __init__(self, note_store: NoteStore):
        """
        Initialize the note prompt provider.

        Args:
            note_store: The note store to use for accessing notes
        """
        self.note_store = note_store
        logger.info("Initialized NotePromptProvider")

    async def list_prompts(self) -> list[types.Prompt]:
        """
        List available prompts.

        Returns:
            List of Prompt objects
        """
        return [
            types.Prompt(
                name="summarize-notes",
                description="Creates a summary of all notes",
                arguments=[
                    types.PromptArgument(
                        name="style",
                        description="Style of the summary (brief/detailed)",
                        required=False,
                    ),
                    types.PromptArgument(
                        name="tag",
                        description="Filter notes by tag",
                        required=False,
                    ),
                ],
            ),
            types.Prompt(
                name="analyze-note",
                description="Analyze a specific note",
                arguments=[
                    types.PromptArgument(
                        name="name",
                        description="Name of the note to analyze",
                        required=True,
                    )
                ],
            ),
        ]

    async def get_prompt(
        self, name: str, arguments: dict[str, str]
    ) -> types.GetPromptResult:
        """
        Generate a prompt by combining arguments with server state.

        Args:
            name: The name of the prompt
            arguments: Dictionary of prompt arguments

        Returns:
            GetPromptResult containing the generated prompt

        Raises:
            PromptGenerationError: If there's an error generating the prompt
            InvalidArgumentError: If invalid arguments are provided
        """
        try:
            if name == "summarize-notes":
                return await self._get_summarize_notes_prompt(arguments)
            elif name == "analyze-note":
                return await self._get_analyze_note_prompt(arguments)
            else:
                logger.error(f"Unknown prompt: {name}")
                raise PromptGenerationError(f"Unknown prompt: {name}")
        except Exception as e:
            logger.error(f"Error generating prompt '{name}': {str(e)}")
            raise PromptGenerationError(f"Error generating prompt: {str(e)}") from e

    async def _get_summarize_notes_prompt(
        self, arguments: dict[str, str]
    ) -> types.GetPromptResult:
        """
        Generate a prompt for summarizing notes.

        Args:
            arguments: Dictionary of prompt arguments

        Returns:
            GetPromptResult for note summarization
        """
        style = arguments.get("style", "brief")
        tag = arguments.get("tag")

        detail_prompt = " Give extensive details." if style == "detailed" else ""

        # Filter notes by tag if specified
        if tag:
            notes_to_summarize = self.note_store.get_by_tag(tag)
            tag_filter_msg = f" filtered by tag '{tag}'"
        else:
            notes_to_summarize = self.note_store.list_all()
            tag_filter_msg = ""

        if not notes_to_summarize:
            return types.GetPromptResult(
                description="No notes found to summarize",
                messages=[
                    types.PromptMessage(
                        role="user",
                        content=types.TextContent(
                            type="text",
                            text=f"There are no notes{tag_filter_msg} to summarize. Please suggest some topics I might want to take notes on.",
                        ),
                    )
                ],
            )

        return types.GetPromptResult(
            description=f"Summarize the current notes{tag_filter_msg}",
            messages=[
                types.PromptMessage(
                    role="user",
                    content=types.TextContent(
                        type="text",
                        text=f"Here are the current notes to summarize{tag_filter_msg}:{detail_prompt}\n\n"
                        + "\n".join(
                            f"- {note.name} (created {note.created_at.isoformat()}): {note.content}"
                            for note in notes_to_summarize
                        ),
                    ),
                )
            ],
        )

    async def _get_analyze_note_prompt(
        self, arguments: dict[str, str]
    ) -> types.GetPromptResult:
        """
        Generate a prompt for analyzing a specific note.

        Args:
            arguments: Dictionary of prompt arguments

        Returns:
            GetPromptResult for note analysis

        Raises:
            InvalidArgumentError: If the name argument is missing
            ResourceNotFoundError: If the note is not found
        """
        note_name = arguments.get("name")
        if not note_name:
            logger.error("Missing required argument: name")
            raise InvalidArgumentError("Missing required argument: name")

        try:
            note = self.note_store.get(note_name)
            return types.GetPromptResult(
                description=f"Analyze note: {note_name}",
                messages=[
                    types.PromptMessage(
                        role="user",
                        content=types.TextContent(
                            type="text",
                            text=f"Please analyze this note titled '{note.name}':\n\n{note.content}\n\n"
                            f"Provide insights on the main themes, key points, and suggest any improvements or follow-up notes.",
                        ),
                    )
                ],
            )
        except ResourceNotFoundError as e:
            logger.error(f"Note not found: {note_name}")
            raise ResourceNotFoundError(f"Note not found: {note_name}") from e
