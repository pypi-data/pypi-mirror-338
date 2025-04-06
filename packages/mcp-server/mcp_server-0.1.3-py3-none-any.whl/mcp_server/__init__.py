"""Math Calculator MCP Server."""

from . import server

__version__ = "0.1.3"

def main():
    """Main entry point for the package."""
    server.mcp.run()

__all__ = ['main', 'server']