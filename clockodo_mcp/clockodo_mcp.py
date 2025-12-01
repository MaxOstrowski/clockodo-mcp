"""Clockodo MCP Server implementation."""

import inspect
from typing import Optional
from mcp.server.fastmcp import FastMCP
from enum import Enum
import requests
from dotenv import load_dotenv
import os
from clockodo_mcp.payload_models import (
    CustomerV3, EntryV2, ProjectV4, ServiceV4, TeamV3, AbsenceV4, SubprojectV3,
    NonbusinessDayV2, OvertimeCarryV3, OvertimeReductionV3, LumpSumServiceV4,
    EntryGroupV2, TargetHourV1, AccessGroupV2, HolidaysQuotumV2, WorkTimeV2, UserReportV1, RegisterV1
)
from clockodo_mcp.undocumented_models import (
    EntryGetParams, CustomerGetParams, ProjectGetParams, ServiceGetParams, TeamGetParams,
    AbsenceGetParams, SubprojectGetParams, HolidayQuotaGetParams, WorkTimeGetParams,
    NonbusinessDayGetParams, OvertimeCarryGetParams, OvertimeReductionGetParams,
    LumpSumServiceGetParams, EntryGroupGetParams, TargetHourGetParams, UserReportGetParams,
    AccessGroupGetParams, RegisterGetParams
)

from clockodo_mcp.undocumented_models import (
    DeleteByIdParams, DeleteByIdDryRunForceParams, DeleteEntryGroupParams
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

# Map Resource enum members to their latest endpoint URLs
RESOURCE_ENDPOINTS = {
    Resource.entry: "https://my.clockodo.com/api/v2/entries",
    Resource.customer: "https://my.clockodo.com/api/v3/customers",
    Resource.project: "https://my.clockodo.com/api/v4/projects",
    Resource.service: "https://my.clockodo.com/api/v4/services",
    Resource.team: "https://my.clockodo.com/api/v3/teams",
    Resource.absence: "https://my.clockodo.com/api/v4/absences",
    Resource.subproject: "https://my.clockodo.com/api/v3/subprojects",
    Resource.holiday_quota: "https://my.clockodo.com/api/v2/holidaysQuota",
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

RESOURCE_POST_PUT_ENDPOINTS = {
    Resource.entry: EntryV2,
    Resource.customer: CustomerV3,
    Resource.project: ProjectV4,
    Resource.service: ServiceV4,
    Resource.team: TeamV3,
    Resource.absence: AbsenceV4,
    Resource.subproject: SubprojectV3,
    Resource.holiday_quota: HolidaysQuotumV2,
    Resource.work_time: WorkTimeV2,
    Resource.nonbusiness_day: NonbusinessDayV2,
    Resource.overtime_carry: OvertimeCarryV3,
    Resource.overtime_reduction: OvertimeReductionV3,
    Resource.lump_sum_service: LumpSumServiceV4,
    Resource.entry_group: EntryGroupV2,
    Resource.target_hour: TargetHourV1,
    Resource.user_report: UserReportV1,
    Resource.access_group: AccessGroupV2,
    Resource.register: RegisterV1,
}


# Dict mapping Resource to GET parameter model
RESOURCE_GET_MODELS = {
    Resource.entry: EntryGetParams,
    Resource.customer: CustomerGetParams,
    Resource.project: ProjectGetParams,
    Resource.service: ServiceGetParams,
    Resource.team: TeamGetParams,
    Resource.absence: AbsenceGetParams,
    Resource.subproject: SubprojectGetParams,
    Resource.holiday_quota: HolidayQuotaGetParams,
    Resource.work_time: WorkTimeGetParams,
    Resource.nonbusiness_day: NonbusinessDayGetParams,
    Resource.overtime_carry: OvertimeCarryGetParams,
    Resource.overtime_reduction: OvertimeReductionGetParams,
    Resource.lump_sum_service: LumpSumServiceGetParams,
    Resource.entry_group: EntryGroupGetParams,
    Resource.target_hour: TargetHourGetParams,
    Resource.user_report: UserReportGetParams,
    Resource.access_group: AccessGroupGetParams,
    Resource.register: RegisterGetParams,
}


RESOURCE_DELETE_MODELS = {
    Resource.entry: DeleteByIdParams,
    Resource.customer: DeleteByIdDryRunForceParams,
    Resource.project: DeleteByIdDryRunForceParams,
    Resource.service: DeleteByIdParams,
    Resource.team: DeleteByIdParams,
    Resource.absence: DeleteByIdParams,
    Resource.subproject: DeleteByIdDryRunForceParams,
    Resource.holiday_quota: DeleteByIdParams,
    Resource.work_time: DeleteByIdParams,
    Resource.nonbusiness_day: DeleteByIdParams,
    Resource.overtime_carry: DeleteByIdParams,
    Resource.overtime_reduction: DeleteByIdParams,
    Resource.lump_sum_service: DeleteByIdDryRunForceParams,
    Resource.entry_group: DeleteEntryGroupParams,
    Resource.target_hour: DeleteByIdParams,
    Resource.user_report: None,
    Resource.access_group: DeleteByIdParams,
    Resource.register: None,
}


def make_tool(action: str, resource, url, model):
        tool_name = f"{action}_{resource.value}"
        sig_params = [
            inspect.Parameter('resource_id', inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=Optional[int], default=None),
            inspect.Parameter('data', inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=Optional[model], default=None)
        ]
        def tool_func(resource_id=None, data=None):
            """
            {action} {resource.value} resource from Clockodo API.

            Args:
                resource_id (Optional[int]): The resource ID for specific resource retrieval.
                data (Optional[{model.__name__}]): additional parameters.

            Returns:
                dict: The API response from Clockodo.
            """
            if action == "get":
                method = "GET"
            elif action == "delete":
                method = "DELETE"
            elif action == "create/update":
                if resource_id is not None:
                    method = "PUT"
                else:
                    method = "POST"
            else:
                raise ValueError(f"Unsupported action: {action}")
            endpoint = f"{url}/{resource_id}" if resource_id else url
            headers = AUTH_HEADERS
            resp = requests.request(method, endpoint, headers=headers, params=data.model_dump() if data else None)
            return resp.json()
        tool_func.__name__ = tool_name
        tool_func.__doc__ = tool_func.__doc__.format(action=action, resource=resource, model=model)
        tool_func.__signature__ = inspect.Signature(sig_params)
        mcp.tool(name=tool_name)(tool_func)

def create_tools():
    # Register three tools per resource: get, delete, post/put
    for resource, url in RESOURCE_ENDPOINTS.items():
        get_model = RESOURCE_GET_MODELS[resource]
        delete_model = RESOURCE_DELETE_MODELS[resource]
        post_put_model = RESOURCE_POST_PUT_ENDPOINTS[resource]

        # GET tool
        if get_model is not None:
            make_tool("get", resource, url, get_model)
        # DELETE tool
        if delete_model is not None:
            make_tool("delete", resource, url, delete_model)
        # POST/PUT tool
        if post_put_model is not None:
            make_tool("create/update", resource, url, post_put_model)

    
def main():
    create_tools()
    mcp.run(transport="stdio")
