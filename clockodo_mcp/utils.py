"""
Utility functions and classes for Clockodo MCP integration.
"""

from enum import Enum
from typing import Optional

from pydantic import BaseModel

from clockodo_mcp.models import AbsenceStatus, AbsenceType, Billable, BudgetSource

class Service(Enum):
    """ All available Clockodo MCP services. """
    targethours = "targethours"
    userreports = "userreports"
    worktimes = "worktimes"
    worktimeschangerequest = "worktimeschangerequest"
    accessgroups_customers = "accessgroups_customers"
    accessgroups_customers_general = "accessgroups_customers_general"
    accessgroups_customersprojects = "accessgroups_customersprojects"
    accessgroups_projects = "accessgroups_projects"
    accessgroups_services = "accessgroups_services"
    accessgroups_services_general = "accessgroups_services_general"
    accessgroups = "accessgroups"
    clock = "clock"
    entries = "entries"
    entries_texts = "entries_texts"
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
    customers_count_projects = "customers_count_projects"
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
    projects_reports = "projects_reports"
    services = "services"

id_endpoint_map = {
    Service.targethours: "/targethours/{id}",
    Service.userreports: "/userreports/{id}",
    Service.accessgroups_customers: "/v2/accessGroups/{id}/customers",
    Service.accessgroups_customers_general: "/v2/accessGroups/{id}/customers/general",
    Service.accessgroups_customersprojects: "/v2/accessGroups/{id}/customersProjects",
    Service.accessgroups_projects: "/v2/accessGroups/{id}/projects",
    Service.accessgroups_services: "/v2/accessGroups/{id}/services",
    Service.accessgroups_services_general: "/v2/accessGroups/{id}/services/general",
    Service.accessgroups: "/v2/accessGroups/{id}",
    Service.clock: "/v2/clock/{id}",
    Service.entries: "/v2/entries/{id}",
    Service.entrygroups: "/v2/entrygroups/{id}",
    Service.holidaysquota: "/v2/holidaysQuota/{id}",
    Service.individualuseraccess_users_clear: "/v2/individualUserAccess/{id}/clear",
    Service.individualuseraccess_users_customers: "/v2/individualUserAccess/{id}/customers",
    Service.individualuseraccess_users_customers_general: "/v2/individualUserAccess/{id}/customers/general",
    Service.individualuseraccess_users_customersprojects: "/v2/individualUserAccess/{id}/customersProjects",
    Service.individualuseraccess_users_projects: "/v2/individualUserAccess/{id}/projects",
    Service.individualuseraccess_users_services: "/v2/individualUserAccess/{id}/services",
    Service.individualuseraccess_users_services_general: "/v2/individualUserAccess/{id}/services/general",
    Service.nonbusinessdays: "/v2/nonbusinessDays/{id}",
    Service.nonbusinessgroups: "/v2/nonbusinessGroups/{id}",
    Service.users_access_customers_projects: "/v2/users/{id}/access/customers-projects",
    Service.users_access_services: "/v2/users/{id}/access/services",
    Service.customers: "/v3/customers/{id}",
    Service.holidayscarry: "/v3/holidaysCarry/{id}",
    Service.overtimecarry: "/v3/overtimeCarry/{id}",
    Service.overtimereductions: "/v3/overtimeReductions/{id}",
    Service.subprojects: "/v3/subprojects/{id}",
    Service.teams: "/v3/teams/{id}",
    Service.users: "/v3/users/{id}",
    Service.usersnonbusinessgroups: "/v3/usersNonbusinessGroups/{id}",
    Service.absences: "/v4/absences/{id}",
    Service.lumpsumservices: "/v4/lumpSumServices/{id}",
    Service.projects: "/v4/projects/{id}",
    Service.services: "/v4/services/{id}",
}


noid_endpoint_map = {
    Service.targethours: "/targethours",
    Service.userreports: "/userreports",
    Service.worktimes: "/v2/workTimes",
    Service.accessgroups: "/v2/accessGroups",
    Service.clock: "/v2/clock",
    Service.entries: "/v2/entries",
    Service.entrygroups: "/v2/entrygroups",
    Service.holidaysquota: "/v2/holidaysQuota",
    Service.nonbusinessdays: "/v2/nonbusinessDays",
    Service.nonbusinessgroups: "/v2/nonbusinessGroups",
    Service.customers: "/v3/customers",
    Service.customers_count_projects: "/v3/customers/countProjects",
    Service.holidayscarry: "/v3/holidaysCarry",
    Service.overtimecarry: "/v3/overtimeCarry",
    Service.overtimereductions: "/v3/overtimeReductions",
    Service.subprojects: "/v3/subprojects",
    Service.teams: "/v3/teams",
    Service.users: "/v3/users",
    Service.usersnonbusinessgroups: "/v3/usersNonbusinessGroups",
    Service.absences: "/v4/absences",
    Service.lumpsumservices: "/v4/lumpSumServices",
    Service.projects: "/v4/projects",
    Service.projects_reports: "/v4/projects/reports",
    Service.services: "/v4/services",
    Service.entries_texts: "/v3/entriesTexts",
}

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

class ApiProjectsReports_SortForIndex(str, Enum):
    customers_name = "customers_name"
    customers_name_desc = "-customers_name"
    projects_name = "projects_name"
    projects_name_desc = "-projects_name"

class ProjectsReportsFilter(BaseModel):
    active: Optional[bool] = None
    fulltext: Optional[str] = None
    budget_source: Optional[list[BudgetSource]] = None


class ServicesFilter(BaseModel):
    active: Optional[bool] = None
    fulltext: Optional[str] = None

class SubprojectsFilter(BaseModel):
    active: Optional[bool] = None
    completed: Optional[bool] = None
    fulltext: Optional[str] = None
    projects_id: Optional[int] = None

class TeamsFilter(BaseModel):
    fulltext: Optional[str] = None

class AbsencesFilter(BaseModel):
    status: Optional[list[AbsenceStatus]] = None
    teams_id: Optional[list[Optional[int]]] = None
    type: Optional[list[AbsenceType]] = None
    users_active: Optional[bool] = None
    users_id: Optional[list[int]] = None
    year: Optional[list[int]] = None



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

