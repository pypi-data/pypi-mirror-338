from .pypi_mcp import mcp

def main() -> None:
    """Entry point for the MCP server."""
    mcp.run()
