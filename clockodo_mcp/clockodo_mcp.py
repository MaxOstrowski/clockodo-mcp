"""Clockodo MCP Server implementation."""

import inspect
from typing import Optional
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from enum import Enum
import requests
from dotenv import load_dotenv
import os
from clockodo_mcp.payload_models import (
    CustomerV3, EntryV2, ProjectV4, ServiceV4, TeamV3, AbsenceV4, SubprojectV3,
    NonbusinessDayV2, OvertimeCarryV3, OvertimeReductionV3, LumpSumServiceV4,
    EntryGroupV2, TargetHourV1, AccessGroupV2, HolidaysQuotumV2, WorkTimeV2, UserReportV1, RegisterV1
)

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
    Resource.entry: ("https://my.clockodo.com/api/v2/entries", EntryV2),
    Resource.customer: ("https://my.clockodo.com/api/v3/customers", CustomerV3),
    Resource.project: ("https://my.clockodo.com/api/v4/projects", ProjectV4),
    Resource.service: ("https://my.clockodo.com/api/v4/services", ServiceV4),
    Resource.team: ("https://my.clockodo.com/api/v3/teams", TeamV3),
    Resource.absence: ("https://my.clockodo.com/api/v4/absences", AbsenceV4),
    Resource.subproject: ("https://my.clockodo.com/api/v3/subprojects", SubprojectV3),
    Resource.holiday_quota: ("https://my.clockodo.com/api/v2/holidaysQuota", HolidaysQuotumV2),
    Resource.work_time: ("https://my.clockodo.com/api/v2/workTimes", WorkTimeV2),
    Resource.nonbusiness_day: ("https://my.clockodo.com/api/v2/nonbusinessDays", NonbusinessDayV2),
    Resource.overtime_carry: ("https://my.clockodo.com/api/v3/overtimeCarry", OvertimeCarryV3),
    Resource.overtime_reduction: ("https://my.clockodo.com/api/v3/overtimeReductions", OvertimeReductionV3),
    Resource.lump_sum_service: ("https://my.clockodo.com/api/v4/lumpSumServices", LumpSumServiceV4),
    Resource.entry_group: ("https://my.clockodo.com/api/v2/entrygroups", EntryGroupV2),
    Resource.target_hour: ("https://my.clockodo.com/api/targethours", TargetHourV1),
    Resource.user_report: ("https://my.clockodo.com/api/userreports", UserReportV1),
    Resource.access_group: ("https://my.clockodo.com/api/v2/accessGroups", AccessGroupV2),
    Resource.register: ("https://my.clockodo.com/api/register", RegisterV1),
}



def _make_tool(resource: Resource, url: str, model: BaseModel):
    tool_name = f"manage_{resource.value}"
    data_type = Optional[model]
    sig_params = [
        inspect.Parameter('action', inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=Action),
        inspect.Parameter('resource_id', inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=Optional[int], default=None),
        inspect.Parameter('data', inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=data_type, default=None)
    ]
    def tool_func(action, resource_id=None, data=None):
        """
        Manage Clockodo {resource.value}.

        Args:
            action (Action): The action to perform (get, create, update, delete).
            resource_id (Optional[int]): The resource ID for single-resource operations.
            data (Optional[{model.__name__}]): The payload for create or update operations.

        Returns:
            dict: The API response from Clockodo.
        """
        headers = AUTH_HEADERS
        base_url = url
        if action == Action.get:
            endpoint = f"{base_url}/{resource_id}" if resource_id else base_url
            resp = requests.get(endpoint, headers=headers)
            return resp.json()
        elif action == Action.create:
            payload = data.model_dump() if hasattr(data, 'model_dump') else data
            resp = requests.post(base_url, headers=headers, json=payload)
            return resp.json()
        elif action == Action.update:
            if resource_id is None:
                return {"error": "resource_id is required for update action"}
            endpoint = f"{base_url}/{resource_id}"
            payload = data.model_dump() if hasattr(data, 'model_dump') else data
            resp = requests.put(endpoint, headers=headers, json=payload)
            return resp.json()
        elif action == Action.delete:
            if resource_id is None:
                return {"error": "resource_id is required for delete action"}
            endpoint = f"{base_url}/{resource_id}"
            resp = requests.delete(endpoint, headers=headers)
            return resp.json()
        else:
            return {"error": "Invalid action"}
    tool_func.__name__ = tool_name
    tool_func.__doc__ = tool_func.__doc__.format(resource=resource, model=model)
    tool_func.__signature__ = inspect.Signature(sig_params)
    mcp.tool(name=tool_name)(tool_func)

for resource, (url, model) in RESOURCE_ENDPOINTS.items():
    _make_tool(resource, url, model)
    
def main():
    mcp.run(transport="stdio")
