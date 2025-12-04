""" get with ID endpoint mapping for clockodo_mcp """

from enum import Enum
from typing import Optional

import requests
from clockodo_mcp.clockodo_mcp import AUTH_HEADERS, mcp, BASE_URL

from clockodo_mcp.spec_models import UserScopeEnum, userreports__id__get_InputModel, UserReportTypeEnum

class ServiceEnum(Enum):
    targethours = "targethours"
    userreports = "userreports"
    accessgroups_customers = "accessgroups_customers"
    accessgroups_customers_general = "accessgroups_customers_general"
    accessgroups_customersprojects = "accessgroups_customersprojects"
    accessgroups_projects = "accessgroups_projects"
    accessgroups_services = "accessgroups_services"
    accessgroups_services_general = "accessgroups_services_general"
    accessgroups = "accessgroups"
    clock = "clock"
    entries = "entries"
    entrygroups = "entrygroups"
    holidaysquota = "holidaysquota"
    individualuseraccess_users_clear = "individualuseraccess_users_clear"
    individualuseraccess_users_customers = "individualuseraccess_users_customers"
    individualuseraccess_users_customers_general = "individualuseraccess_users_customers_general"
    individualuseraccess_users_customersprojects = "individualuseraccess_users_customersprojects"
    individualuseraccess_users_projects = "individualuseraccess_users_projects"
    individualuseraccess_users_services = "individualuseraccess_users_services"
    individualuseraccess_users_services_general = "individualuseraccess_users_services_general"
    nonbusinessdays = "nonbusinessdays"
    nonbusinessgroups = "nonbusinessgroups"
    users_access_customers_projects = "users_access_customers_projects"
    users_access_services = "users_access_services"
    customers = "customers"
    holidayscarry = "holidayscarry"
    overtimecarry = "overtimecarry"
    overtimereductions = "overtimereductions"
    subprojects = "subprojects"
    teams = "teams"
    users = "users"
    usersnonbusinessgroups = "usersnonbusinessgroups"
    absences = "absences"
    lumpsumservices = "lumpsumservices"
    projects = "projects"
    services = "services"

id_endpoint_map = {
    ServiceEnum.targethours: "/targethours/{id}",
    ServiceEnum.userreports: "/userreports/{id}",
    ServiceEnum.accessgroups_customers: "/v2/accessGroups/{id}/customers",
    ServiceEnum.accessgroups_customers_general: "/v2/accessGroups/{id}/customers/general",
    ServiceEnum.accessgroups_customersprojects: "/v2/accessGroups/{id}/customersProjects",
    ServiceEnum.accessgroups_projects: "/v2/accessGroups/{id}/projects",
    ServiceEnum.accessgroups_services: "/v2/accessGroups/{id}/services",
    ServiceEnum.accessgroups_services_general: "/v2/accessGroups/{id}/services/general",
    ServiceEnum.accessgroups: "/v2/accessGroups/{id}",
    ServiceEnum.clock: "/v2/clock/{id}",
    ServiceEnum.entries: "/v2/entries/{id}",
    ServiceEnum.entrygroups: "/v2/entrygroups/{id}",
    ServiceEnum.holidaysquota: "/v2/holidaysQuota/{id}",
    ServiceEnum.individualuseraccess_users_clear: "/v2/individualUserAccess/{id}/clear",
    ServiceEnum.individualuseraccess_users_customers: "/v2/individualUserAccess/{id}/customers",
    ServiceEnum.individualuseraccess_users_customers_general: "/v2/individualUserAccess/{id}/customers/general",
    ServiceEnum.individualuseraccess_users_customersprojects: "/v2/individualUserAccess/{id}/customersProjects",
    ServiceEnum.individualuseraccess_users_projects: "/v2/individualUserAccess/{id}/projects",
    ServiceEnum.individualuseraccess_users_services: "/v2/individualUserAccess/{id}/services",
    ServiceEnum.individualuseraccess_users_services_general: "/v2/individualUserAccess/{id}/services/general",
    ServiceEnum.nonbusinessdays: "/v2/nonbusinessDays/{id}",
    ServiceEnum.nonbusinessgroups: "/v2/nonbusinessGroups/{id}",
    ServiceEnum.users_access_customers_projects: "/v2/users/{id}/access/customers-projects",
    ServiceEnum.users_access_services: "/v2/users/{id}/access/services",
    ServiceEnum.customers: "/v3/customers/{id}",
    ServiceEnum.holidayscarry: "/v3/holidaysCarry/{id}",
    ServiceEnum.overtimecarry: "/v3/overtimeCarry/{id}",
    ServiceEnum.overtimereductions: "/v3/overtimeReductions/{id}",
    ServiceEnum.subprojects: "/v3/subprojects/{id}",
    ServiceEnum.teams: "/v3/teams/{id}",
    ServiceEnum.users: "/v3/users/{id}",
    ServiceEnum.usersnonbusinessgroups: "/v3/usersNonbusinessGroups/{id}",
    ServiceEnum.absences: "/v4/absences/{id}",
    ServiceEnum.lumpsumservices: "/v4/lumpSumServices/{id}",
    ServiceEnum.projects: "/v4/projects/{id}",
    ServiceEnum.services: "/v4/services/{id}",
}

@mcp.tool()
def get(id: int, service: ServiceEnum) -> dict:
    """ Get entity by ID """
    endpoint_template = id_endpoint_map.get(service)
    if not endpoint_template:
        raise ValueError(f"No endpoint mapping found for service: {service.value}")
    endpoint = endpoint_template.format(id=id)
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS)
    return resp.json()


@mcp.tool()
def get_userreports(id: int, year: int, type: UserReportTypeEnum) -> dict:
    """Get userreport by ID, year, and type"""
    userreports__id__get_InputModel(id=id, year=year, type=type)
    endpoint_template = id_endpoint_map.get(ServiceEnum.userreports)
    endpoint = endpoint_template.format(id=id)
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params={"year": year, "type": type.value})
    return resp.json()

# /v2/nonbusinessDays/{id}
# Path parameter:
# id: integer, required, example: 1, format: int64
# Query parameters:
# year: integer, not required, minimum: 2000, maximum: 2037


@mcp.tool()
def get_nonbusinessdays(id: int, year: Optional[int]) -> dict:
    """ Get nonbusinessdays by ID and optional year """
    endpoint_template = id_endpoint_map.get(ServiceEnum.nonbusinessdays)
    endpoint = endpoint_template.format(id=id)
    params = {}
    if year is not None:
        params["year"] = year
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=params)
    return resp.json()

# /v3/users/{id}
# Path parameter:
# id: integer, required, example: 1, format: int64
# Query parameters:
# scope: $ref: #/components/schemas/UserScope, not required

@mcp.tool()
def get_users(id: int, scope: Optional[UserScopeEnum]) -> dict:
    """ Get users by ID and optional scope """
    endpoint_template = id_endpoint_map.get(ServiceEnum.users)
    endpoint = endpoint_template.format(id=id)
    params = {}
    if scope is not None:
        params["scope"] = scope.value
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=params)
    return resp.json()