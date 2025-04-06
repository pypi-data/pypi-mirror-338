# math_server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def Ajouter(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

@mcp.tool()
def Multiplier(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def diviser(a: float, b: float) -> float:
    """Divide two numbers"""
    if b!=0 :
        return a / b
    else :return None

if __name__ == "__main__":
    mcp.run(transport="stdio")