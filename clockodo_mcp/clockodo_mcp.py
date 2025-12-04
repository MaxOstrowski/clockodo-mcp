"""Clockodo MCP Server implementation."""

from mcp.server.fastmcp import FastMCP
from enum import Enum
import requests
from dotenv import load_dotenv
import os



load_dotenv()
AUTH_HEADERS = {
    "X-ClockodoApiUser": os.getenv("CLOCKODO_API_USER"),
    "X-ClockodoApiKey": os.getenv("CLOCKODO_API_KEY"),
    "X-Clockodo-External-Application": os.getenv("CLOCKODO_EXTERNAL_APP"),
}
mcp = FastMCP("Clockodo MCP Server", json_response=True)
BASE_URL = "https://my.clockodo.com/api"


def main():
    mcp.run(transport="stdio")
