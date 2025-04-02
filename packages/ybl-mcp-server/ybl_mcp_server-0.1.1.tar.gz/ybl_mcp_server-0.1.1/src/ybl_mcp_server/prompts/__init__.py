"""Prompt providers for the ybl-mcp server."""

from .base import PromptProvider
from .note_prompts import NotePromptProvider

__all__ = ["PromptProvider", "NotePromptProvider"]
