#!/usr/bin/env python3

"""
Standalone entry point script for the MCP server.
This avoids module import warnings and provides a clean entry point.
"""

def main():
    # Import and run the server directly
    from mcp_server.server import mcp
    mcp.run()

if __name__ == "__main__":
    main()