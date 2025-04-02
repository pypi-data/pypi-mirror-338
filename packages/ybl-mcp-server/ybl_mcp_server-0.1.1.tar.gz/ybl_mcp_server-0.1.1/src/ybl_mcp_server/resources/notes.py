"""Note resource provider implementation."""

from mcp import types
from pydantic import AnyUrl

from ybl_mcp_server.utils import logger

from ..exceptions import ResourceAccessError, ResourceNotFoundError
from ..models import NoteStore
from .base import ResourceProvider


class NoteResourceProvider(ResourceProvider):
    """Provider for note resources."""

    def __init__(self, note_store: NoteStore):
        """
        Initialize the note resource provider.

        Args:
            note_store: The note store to use for accessing notes
        """
        self.note_store = note_store
        logger.info("Initialized NoteResourceProvider")

    async def list_resources(self) -> list[types.Resource]:
        """
        List available note resources.

        Returns:
            List of Resource objects representing notes
        """
        try:
            resources = [
                types.Resource(
                    uri=AnyUrl(f"note://internal/{note.name}"),
                    name=f"Note: {note.name}",
                    description=f"A note created on {note.created_at.isoformat()}",
                    mimeType="text/plain",
                )
                for note in self.note_store.list_all()
            ]
            logger.debug(f"Listed {len(resources)} note resources")
            return resources
        except Exception as e:
            logger.error(f"Error listing resources: {str(e)}")
            # Return empty list on error rather than failing completely
            return []

    async def read_resource(self, uri: AnyUrl) -> str:
        """
        Read a specific note's content by its URI.

        Args:
            uri: The URI of the note to read

        Returns:
            The note content as a string

        Raises:
            ResourceAccessError: If the URI scheme is not supported
            ResourceNotFoundError: If the note is not found
        """
        if uri.scheme != "note":
            logger.error(f"Unsupported URI scheme: {uri.scheme}")
            raise ResourceAccessError(f"Unsupported URI scheme: {uri.scheme}")

        path = uri.path
        if path is not None:
            name = path.lstrip("/")
            try:
                note = self.note_store.get(name)
                logger.debug(f"Read resource: {uri}")
                return note.content
            except ResourceNotFoundError as e:
                logger.error(f"Note not found: {name}")
                raise ResourceNotFoundError(f"Note not found: {name}") from e
        logger.error(f"Invalid note URI: {uri}")
        raise ResourceAccessError(f"Invalid note URI: {uri}")
