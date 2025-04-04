print("🚀 server.py started")

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math Assistant")

@mcp.tool()
def add(x: float, y: float) -> float:
    return x + y

@mcp.tool()
def subtract(x: float, y: float) -> float:
    return x - y

@mcp.tool()
def multiply(x: float, y: float) -> float:
    return x * y

@mcp.tool()
def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    print("🔧 main() called")
    mcp.run()

if __name__ == "__main__":
    print("👋 running as __main__")
    main()
