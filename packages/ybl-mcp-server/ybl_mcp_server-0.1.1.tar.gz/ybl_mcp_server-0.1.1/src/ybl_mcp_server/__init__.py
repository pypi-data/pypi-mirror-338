"""Main entry point for the ybl-mcp-server package."""

import asyncio

from . import server


def main():
    """Main entry point for the package."""
    asyncio.run(server.main())


# Expose important items at package level
__all__ = ["main", "server"]
