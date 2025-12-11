"""Clockodo MCP Server implementation."""

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os

load_dotenv()
AUTH_HEADERS = {
    "X-ClockodoApiUser": os.getenv("CLOCKODO_API_USER"),
    "X-ClockodoApiKey": os.getenv("CLOCKODO_API_KEY"),
    "X-Clockodo-External-Application": os.getenv("CLOCKODO_EXTERNAL_APP"),
}

BASE_URL = "https://my.clockodo.com/api"

class ToolRestrictor:
    def __init__(self):
        self.collected_tools = []
        self.mcp = FastMCP("""Clockodo MCP Server
This MCP server provides integration with the Clockodo time tracking API.
It allows querying, creating, and updating time entries (entries), users, projects(subprojects), and more.
Use this server to automate and analyze your time tracking data.""", json_response=True)

    def tool(self, flag: str = "default"):
        def decorator(func):
            #self.mcp.tool(*args, **kwargs)(func)
            self.collected_tools.append((func, flag))
            return func
        return decorator
    
    def register_tools(self, restricted: bool = False):
        for func, flag in self.collected_tools:
            if restricted and flag == "restricted":
                continue
            self.mcp.tool()(func)
    
mcp = ToolRestrictor()
