"""MCP Math Server implementation."""
import sys

from mcp.server.fastmcp import FastMCP

# Add more detailed logging
print("🚀 mcp_math_server.server module starting", file=sys.stderr)

mcp = FastMCP("Math Assistant")

@mcp.tool()
def add(x: float, y: float) -> float:
    """Add two numbers together."""
    print(f"Adding {x} + {y}", file=sys.stderr)
    return x + y

@mcp.tool()
def subtract(x: float, y: float) -> float:
    """Subtract y from x."""
    print(f"Subtracting {y} from {x}", file=sys.stderr)
    return x - y

@mcp.tool()
def multiply(x: float, y: float) -> float:
    """Multiply two numbers together."""
    print(f"Multiplying {x} × {y}", file=sys.stderr)
    return x * y

@mcp.tool()
def divide(x: float, y: float) -> float:
    """Divide x by y."""
    print(f"Dividing {x} ÷ {y}", file=sys.stderr)
    if y == 0:
        print("ERROR: Division by zero attempted", file=sys.stderr)
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    """Run the MCP server."""
    print("🔧 mcp_math_server.server.main() called", file=sys.stderr)
    try:
        mcp.run()
    except Exception as e:
        print(f"ERROR in MCP server: {str(e)}", file=sys.stderr)
        raise

if __name__ == "__main__":
    print("👋 mcp_math_server.server running as __main__", file=sys.stderr)
    main()
