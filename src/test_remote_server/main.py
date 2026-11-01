from fastmcp import FastMCP
import json

# Create the FastMCP server instance
mcp = FastMCP("Simple Calculator Server")

# Tool: Add two numbers
@mcp.tool
def add (a: int, b: int) -> int:
    """Add two numbers together.
    Args:
        a: First number
        b: Second number
    Returns:
        The sum of a and b
    """
    return a + b

# Resource: Server information
@mcp. resource("info://server")
def server_info() -> str:
    """Get information about this server."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add", "random_number"],
        "author": "Your Name"
    }
    return json.dumps (info, indent=2)

# Start the server
if __name__ == "__main__":
    from test_remote_server import main
    main()