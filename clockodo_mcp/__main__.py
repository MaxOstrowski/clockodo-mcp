import clockodo_mcp.clockodo_mcp
import clockodo_mcp.get # important to load get tools
import clockodo_mcp.delete # important to load delete tools

def main():
    clockodo_mcp.clockodo_mcp.mcp.run(transport="stdio")

if __name__ == "__main__":
    main()