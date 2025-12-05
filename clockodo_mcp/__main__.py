import clockodo_mcp.clockodo_mcp
import clockodo_mcp.get_id

def main():
    clockodo_mcp.clockodo_mcp.mcp.run(transport="stdio")

if __name__ == "__main__":
    main()