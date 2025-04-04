from mcp.server.fastmcp import FastMCP

# Create your MCP server
mcp = FastMCP("Math Assistant")

@mcp.tool()
def add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y

@mcp.tool()
def subtract(x: float, y: float) -> float:
    """Subtract y from x."""
    return x - y

@mcp.tool()
def multiply(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y

@mcp.tool()
def divide(x: float, y: float) -> float:
    """Divide x by y. Returns a message if dividing by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    """Entry point for CLI command"""
    mcp.run()

if __name__ == "__main__":
    main()
