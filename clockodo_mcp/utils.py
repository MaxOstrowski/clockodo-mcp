"""
Utility functions and classes for Clockodo MCP integration.
"""

from enum import Enum
from typing import Optional

from pydantic import BaseModel

from clockodo_mcp.models import Billable, BudgetSource

class ServiceEnum(Enum):
    """ All available Clockodo MCP services. """
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


noid_endpoint_map = {
    ServiceEnum.targethours: "/targethours",
    ServiceEnum.userreports: "/userreports",
    ServiceEnum.accessgroups: "/v2/accessGroups",
    ServiceEnum.clock: "/v2/clock",
    ServiceEnum.entries: "/v2/entries",
    ServiceEnum.entrygroups: "/v2/entrygroups",
    ServiceEnum.holidaysquota: "/v2/holidaysQuota",
    ServiceEnum.nonbusinessdays: "/v2/nonbusinessDays",
    ServiceEnum.nonbusinessgroups: "/v2/nonbusinessGroups",
    ServiceEnum.customers: "/v3/customers",
    ServiceEnum.holidayscarry: "/v3/holidaysCarry",
    ServiceEnum.overtimecarry: "/v3/overtimeCarry",
    ServiceEnum.overtimereductions: "/v3/overtimeReductions",
    ServiceEnum.subprojects: "/v3/subprojects",
    ServiceEnum.teams: "/v3/teams",
    ServiceEnum.users: "/v3/users",
    ServiceEnum.usersnonbusinessgroups: "/v3/usersNonbusinessGroups",
    ServiceEnum.absences: "/v4/absences",
    ServiceEnum.lumpsumservices: "/v4/lumpSumServices",
    ServiceEnum.projects: "/v4/projects",
    ServiceEnum.services: "/v4/services",
}


class ServiceEnumListAuto(Enum):
    CUSTOMERS = "/v3/customers"
    CUSTOMERS_COUNT_PROJECTS = "/v3/customers/countProjects"
    ENTRIES_TEXTS = "/v3/entriesTexts"
    HOLIDAYS_CARRY = "/v3/holidaysCarry"
    OVERTIME_CARRY = "/v3/overtimeCarry"
    OVERTIME_REDUCTIONS = "/v3/overtimeReductions"
    PROJECTS_REPORTS = "/v3/projects/reports"
    SUBPROJECTS = "/v3/subprojects"
    TEAMS = "/v3/teams"
    USERS_ALL = "/v3/users"
    USERS_NONBUSINESS_GROUPS = "/v3/usersNonbusinessGroups"
    ABSENCES = "/v4/absences"
    LUMPSUM_SERVICES = "/v4/lumpSumServices"
    PROJECTS = "/v4/projects"
    PROJECTS_REPORTS_V4 = "/v4/projects/reports"
    SERVICES = "/v4/services"

# TODO:
# /v2/workTimes/changeRequests/{id}/approve
# /v3/workTimes/changeRequests/{id}/approve
# /v2/workTimes/changeRequests/{id}/decline
# /v3/projects/{id}/setBilled
# /v3/subprojects/{id}/complete
# /v4/projects/{id}/complete
# /v4/projects/reports


class ApiUsersV3_SortForIndex(str, Enum):
    active = "active"
    active_desc = "-active"
    id = "id"
    id_desc = "-id"
    name = "name"
    name_desc = "-name"
    number = "number"
    number_desc = "-number"
    role = "role"
    role_desc = "-role"
    teams_name = "teams_name"
    teams_name_desc = "-teams_name"


class EntriesTextFilter(BaseModel):
    billable: Optional[Billable] = None
    customers_id: Optional[int] = None
    day: Optional[str] = None  # Date string
    projects_id: Optional[list[int]] = None
    services_id: Optional[list[int]] = None
    time_since: Optional[str] = None  # Date string
    time_until: Optional[str] = None  # Date string
    users_id: Optional[list[int]] = None

class CustomerFilter(BaseModel):
    active: Optional[bool] = None
    fulltext: Optional[str] = None

class UsersFilter(BaseModel):
    active: Optional[bool] = None
    fulltext: Optional[str] = None
    teams_id: Optional[list[Optional[int]]] = None

class UsersNonbusinessGroupsFilter(BaseModel):
    nonbusiness_groups_id: Optional[list[int]] = None
    users_id: Optional[list[int]] = None

class LumpSumServicesFilter(BaseModel):
    active: Optional[bool] = None
    fulltext: Optional[str] = None


class ProjectsFilter(BaseModel):
    active: Optional[bool] = None
    completed: Optional[bool] = None
    customers_id: Optional[int] = None
    fulltext: Optional[str] = None

class ApiProjectsReportsV4_SortForIndex(str, Enum):
    customers_name = "customers_name"
    customers_name_desc = "-customers_name"
    projects_name = "projects_name"
    projects_name_desc = "-projects_name"

class ProjectsReportsV4Filter(BaseModel):
    active: Optional[bool] = None
    fulltext: Optional[str] = None
    budget_source: Optional[list[BudgetSource]] = None


class ServicesFilter(BaseModel):
    active: Optional[bool] = None
    fulltext: Optional[str] = None


def flatten_dict(d: dict, parent_key: str =''):
    """
    Recursively flattens a dictionary for query parameters using bracket notation, e.g. filter[active]=True.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}[{k}]" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key).items())
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, new_key).items())
                elif isinstance(item, bool):
                    items.append((new_key, str(item).lower()))
                else:
                    items.append((new_key, item))
        elif isinstance(v, bool):
            items.append((new_key, str(v).lower()))
        else:
            items.append((new_key, v))
    return dict(items)

