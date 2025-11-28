"""Clockodo MCP Server implementation."""

from typing import Optional
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from enum import Enum
import requests
from dotenv import load_dotenv
import os
from clockodo_mcp.payload_models import CustomerV3

load_dotenv()
AUTH_HEADERS = {
    "X-ClockodoApiUser": os.getenv("CLOCKODO_API_USER"),
    "X-ClockodoApiKey": os.getenv("CLOCKODO_API_KEY"),
    "X-Clockodo-External-Application": os.getenv("CLOCKODO_EXTERNAL_APP"),
}
mcp = FastMCP("Clockodo MCP Server", json_response=True)

class Action(str, Enum):
    get = "get"
    create = "create"
    update = "update"
    delete = "delete"


class Resource(str, Enum):
    entry = "entry"
    customer = "customer"
    project = "project"
    service = "service"
    team = "team"
    absence = "absence"
    subproject = "subproject"
    holiday_quota = "holiday_quota"
    work_time = "work_time"
    nonbusiness_day = "nonbusiness_day"
    overtime_carry = "overtime_carry"
    overtime_reduction = "overtime_reduction"
    lump_sum_service = "lump_sum_service"
    entry_group = "entry_group"
    target_hour = "target_hour"
    user_report = "user_report"
    access_group = "access_group"
    register = "register"

class ResourceRequest(BaseModel):
    """
    Request model for managing Clockodo resources."""

    resource: Resource = Field(
        ..., description="The resource to manage"
    )
    action: Action = Field(
        ..., description="Action to perform"
    )
    resource_id: int | None = Field(
        None, description="ID of the resource for single-resource operations (get, update, delete) or None for all resources."
    )
    data: dict | None = Field(
        None, description="Payload for create or update operations."
    )


# Map Resource enum members to their latest endpoint URLs
RESOURCE_ENDPOINTS = {
    Resource.entry: "https://my.clockodo.com/api/v2/entries",
    Resource.customer: "https://my.clockodo.com/api/v3/customers",
    Resource.project: "https://my.clockodo.com/api/v4/projects",
    Resource.service: "https://my.clockodo.com/api/v4/services",
    Resource.team: "https://my.clockodo.com/api/v3/teams",
    Resource.absence: "https://my.clockodo.com/api/v4/absences",
    Resource.subproject: "https://my.clockodo.com/api/v3/subprojects",
    Resource.holiday_quota: "https://my.clockodo.com/api/v3/holidaysQuota",
    Resource.work_time: "https://my.clockodo.com/api/v2/workTimes",
    Resource.nonbusiness_day: "https://my.clockodo.com/api/v2/nonbusinessDays",
    Resource.overtime_carry: "https://my.clockodo.com/api/v3/overtimeCarry",
    Resource.overtime_reduction: "https://my.clockodo.com/api/v3/overtimeReductions",
    Resource.lump_sum_service: "https://my.clockodo.com/api/v4/lumpSumServices",
    Resource.entry_group: "https://my.clockodo.com/api/v2/entrygroups",
    Resource.target_hour: "https://my.clockodo.com/api/targethours",
    Resource.user_report: "https://my.clockodo.com/api/userreports",
    Resource.access_group: "https://my.clockodo.com/api/v2/accessGroups",
    Resource.register: "https://my.clockodo.com/api/register",
}


@mcp.tool()
def manage_resource(request: ResourceRequest) -> dict:
    """
    Manage any Clockodo resource via a unified tool.

    Returns:
        dict: The API response from Clockodo.
    """
    headers = AUTH_HEADERS
    base_url = RESOURCE_ENDPOINTS.get(request.resource)
    if not base_url:
        return {"error": f"Unknown resource: {request.resource}"}

    if request.action == Action.get:
        url = f"{base_url}/{request.resource_id}" if request.resource_id else base_url
        resp = requests.get(url, headers=headers)
        return resp.json()
    elif request.action == Action.create:
        resp = requests.post(base_url, headers=headers, json=request.data)
        return resp.json()
    elif request.action == Action.update:
        url = f"{base_url}/{request.resource_id}"
        resp = requests.put(url, headers=headers, json=request.data)
        return resp.json()
    elif request.action == Action.delete:
        url = f"{base_url}/{request.resource_id}"
        resp = requests.delete(url, headers=headers)
        return resp.json()
    else:
        return {"error": "Invalid action"}


@mcp.tool()
def manage_customer(action: Action, customer_id: Optional[int] = None, data: Optional[CustomerV3] = None) -> dict:
    """
    Manage Clockodo customers.

    Args:
        action (Action): The action to perform (get, create, update, delete).
        customer_id (Optional[int]): The customer ID for single-resource operations.
        data (Optional[CustomerV3]): The payload for create or update operations.

    Returns:
        dict: The API response from Clockodo.
    """
    headers = AUTH_HEADERS
    base_url = RESOURCE_ENDPOINTS[Resource.customer]
    if action == Action.get:
        url = f"{base_url}/{customer_id}" if customer_id else base_url
        resp = requests.get(url, headers=headers)
        return resp.json()
    elif action == Action.create:
        resp = requests.post(base_url, headers=headers, json=data.model_dump())
        return resp.json()
    elif action == Action.update:
        if customer_id is None:
            return {"error": "customer_id is required for update action"}
        url = f"{base_url}/{customer_id}"
        resp = requests.put(url, headers=headers, json=data.model_dump())
        return resp.json()
    elif action == Action.delete:
        if customer_id is None:
            return {"error": "customer_id is required for delete action"}
        url = f"{base_url}/{customer_id}"
        resp = requests.delete(url, headers=headers)
        return resp.json()
    else:
        return {"error": "Invalid action"}
    

def main():
    mcp.run(transport="stdio")