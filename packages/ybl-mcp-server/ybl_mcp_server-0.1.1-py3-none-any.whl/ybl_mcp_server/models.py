"""Data models for the ybl-mcp server."""

from datetime import datetime

from pydantic import BaseModel, Field

from ybl_mcp_server.utils import logger

from .exceptions import DuplicateResourceError, ResourceNotFoundError


class Note(BaseModel):
    """Model representing a note with metadata."""

    name: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    tags: set[str] = Field(default_factory=set)

    def update_content(self, new_content: str) -> None:
        """
        Update note content and set the updated_at timestamp.

        Args:
            new_content: The new content for the note
        """
        self.content = new_content
        self.updated_at = datetime.utcnow()

    def add_tag(self, tag: str) -> None:
        """
        Add a tag to the note.

        Args:
            tag: The tag to add
        """
        self.tags.add(tag.lower())

    def remove_tag(self, tag: str) -> None:
        """
        Remove a tag from the note if it exists.

        Args:
            tag: The tag to remove
        """
        self.tags.discard(tag.lower())


class NoteStore:
    """Repository for managing notes."""

    def __init__(self):
        """Initialize an empty note store."""
        self._notes: dict[str, Note] = {}
        logger.info("Initialized NoteStore")

    def add(self, name: str, content: str, tags: list[str] | None = None) -> Note:
        """
        Add a new note to the store.

        Args:
            name: The note name (must be unique)
            content: The note content
            tags: Optional list of tags for the note

        Returns:
            The created Note instance

        Raises:
            DuplicateResourceError: If a note with the same name already exists
        """
        if name in self._notes:
            logger.error(f"Attempted to add duplicate note: {name}")
            raise DuplicateResourceError(f"Note with name '{name}' already exists")

        note = Note(
            name=name, content=content, tags=set(tag.lower() for tag in (tags or []))
        )
        self._notes[name] = note
        logger.info(f"Added note: {name} with {len(tags or [])} tags")
        return note

    def get(self, name: str) -> Note:
        """
        Get a note by name.

        Args:
            name: The name of the note to retrieve

        Returns:
            The Note instance

        Raises:
            ResourceNotFoundError: If no note with the given name exists
        """
        if name not in self._notes:
            logger.error(f"Attempted to access non-existent note: {name}")
            raise ResourceNotFoundError(f"Note with name '{name}' not found")
        return self._notes[name]

    def update(self, name: str, content: str) -> Note:
        """
        Update an existing note's content.

        Args:
            name: The name of the note to update
            content: The new content

        Returns:
            The updated Note instance

        Raises:
            ResourceNotFoundError: If no note with the given name exists
        """
        note = self.get(name)
        note.update_content(content)
        logger.info(f"Updated note: {name}")
        return note

    def delete(self, name: str) -> None:
        """
        Delete a note by name.

        Args:
            name: The name of the note to delete

        Raises:
            ResourceNotFoundError: If no note with the given name exists
        """
        if name not in self._notes:
            logger.error(f"Attempted to delete non-existent note: {name}")
            raise ResourceNotFoundError(f"Note with name '{name}' not found")
        del self._notes[name]
        logger.info(f"Deleted note: {name}")

    def list_all(self) -> list[Note]:
        """
        List all notes.

        Returns:
            List of all Note instances
        """
        return list(self._notes.values())

    def search(self, keyword: str) -> list[Note]:
        """
        Search notes by keyword in content, name, or tags.

        Args:
            keyword: The search keyword

        Returns:
            List of matching Note instances
        """
        keyword = keyword.lower()
        results = [
            note
            for note in self._notes.values()
            if keyword in note.name.lower()
            or keyword in note.content.lower()
            or any(keyword in tag for tag in note.tags)
        ]
        logger.debug(f"Search for '{keyword}' found {len(results)} results")
        return results

    def get_by_tag(self, tag: str) -> list[Note]:
        """
        Get all notes with a specific tag.

        Args:
            tag: The tag to filter by

        Returns:
            List of Note instances with the specified tag
        """
        tag = tag.lower()
        results = [note for note in self._notes.values() if tag in note.tags]
        logger.debug(f"Filter by tag '{tag}' found {len(results)} results")
        return results
