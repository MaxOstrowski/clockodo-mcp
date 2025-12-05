""" get with ID endpoint mapping for clockodo_mcp """

from enum import Enum
from typing import Optional, List, Dict

from pydantic import BaseModel
import requests
from clockodo_mcp.clockodo_mcp import AUTH_HEADERS, mcp, BASE_URL

from clockodo_mcp.models import (
    AbsenceStatus, AbsenceType, Billable, BudgetSource, UserScope, UserReportType, CustomerProjectScope, EntryTextMode, ServiceScope, SortIdName, SortIdNameActive
)

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


class ServiceEnumList(Enum):
    targethours = ServiceEnum.targethours.value
    userreports = ServiceEnum.userreports.value
    accessgroups = ServiceEnum.accessgroups.value
    clock = ServiceEnum.clock.value
    entries = ServiceEnum.entries.value
    entrygroups = ServiceEnum.entrygroups.value
    holidaysquota = ServiceEnum.holidaysquota.value
    nonbusinessdays = ServiceEnum.nonbusinessdays.value
    nonbusinessgroups = ServiceEnum.nonbusinessgroups.value
    customers = ServiceEnum.customers.value
    holidayscarry = ServiceEnum.holidayscarry.value
    overtimecarry = ServiceEnum.overtimecarry.value
    overtimereductions = ServiceEnum.overtimereductions.value
    subprojects = ServiceEnum.subprojects.value
    teams = ServiceEnum.teams.value
    users = ServiceEnum.users.value
    usersnonbusinessgroups = ServiceEnum.usersnonbusinessgroups.value
    absences = ServiceEnum.absences.value
    lumpsumservices = ServiceEnum.lumpsumservices.value
    projects = ServiceEnum.projects.value
    services = ServiceEnum.services.value

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

@mcp.tool()
def get_all(service: ServiceEnumList) -> dict:
    """ Get all entities for a given service """
    endpoint = noid_endpoint_map.get(service)
    if not endpoint:
        raise ValueError(f"No endpoint mapping found for service: {service.value}")
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS)
    return resp.json()

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
def get_userreports(id: int, year: int, type: Optional[UserReportType]) -> dict:
    """
    Get userreport by ID, year, and type.

    Args:
            id (int): The user report ID. Example: 1
            year (int): The year for the report. Required. Minimum: 1910, Maximum: 2026
            type (Optional[UserReportType]): The report type (UserReportType enum). Optional.

    Returns:
            dict: The user report data as returned by the API.
    """
    endpoint_template = id_endpoint_map.get(ServiceEnum.userreports)
    endpoint = endpoint_template.format(id=id)
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params={"year": year, "type": type.value})
    return resp.json()

@mcp.tool()
def get_nonbusinessdays(id: int, year: Optional[int]) -> dict:
    """
    Get nonbusinessdays by ID and optional year.

    Args:
        id (int): The nonbusiness day ID. Required. Example: 1
        year (Optional[int]): The year (optional). Minimum: 2000, Maximum: 2037

    Returns:
        dict: The nonbusiness day data as returned by the API.
    """
    endpoint_template = id_endpoint_map.get(ServiceEnum.nonbusinessdays)
    endpoint = endpoint_template.format(id=id)
    params = {}
    if year is not None:
        params["year"] = year
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=params)
    return resp.json()



@mcp.tool()
def get_users(id: int, scope: Optional[UserScope]) -> dict:
    """
    Get user by ID and optional scope.

    Args:
        id (int): The user ID. Required. Example: 1
        scope (Optional[UserScope]): The user scope 

    Returns:
        dict: The user data as returned by the API.
    """
    endpoint_template = id_endpoint_map.get(ServiceEnum.users)
    endpoint = endpoint_template.format(id=id)
    params = {}
    if scope is not None:
        params["scope"] = scope.value
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=params)
    return resp.json()



# --- AUTO-GENERATED TOOLS FOR PARAMETERIZED ENDPOINTS ---

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

class CustomerFilter(BaseModel):
    active: Optional[bool] = None
    fulltext: Optional[str] = None

@mcp.tool()
def get_customers(
    filter: Optional[CustomerFilter] = None,
    sort: Optional[List[SortIdNameActive]] = None,
    scope: Optional[CustomerProjectScope] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get customers with optional filtering, sorting, and paging.
    Args:
        filter (CustomerFilter, optional): Filter object
        sort (list, optional): List of SortIdNameActive.
        scope (str, optional): CustomerProjectScope.
        page (int, optional): Page number, min 1.
        items_per_page (int, optional): Items per page, min 1, max 5000.
    Returns:
        dict: Customers data.
    """
    params = {}
    if filter is not None:
        params['filter'] = filter.model_dump(exclude_none=True)
    if sort is not None:
        params['sort'] = sort
    if scope is not None:
        params['scope'] = scope
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.CUSTOMERS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

@mcp.tool()
def get_customers_count_projects(
    customers_id: Optional[List[int]] = None,
    scope: Optional[CustomerProjectScope] = None
) -> dict:
    """
    Get customer project counts.
    Args:
        customers_id (list, optional): List of customer IDs (int), min 0, max 500.
        scope (str, optional): CustomerProjectScope.
    Returns:
        dict: Project count data.
    """
    params = {}
    if customers_id is not None:
        params['customers_id'] = customers_id
    if scope is not None:
        params['scope'] = scope
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.CUSTOMERS_COUNT_PROJECTS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()


class EntriesTextFilter(BaseModel):
    billable: Optional[Billable] = None
    customers_id: Optional[int] = None
    day: Optional[str] = None  # Date string
    projects_id: Optional[List[int]] = None
    services_id: Optional[List[int]] = None
    time_since: Optional[str] = None  # Date string
    time_until: Optional[str] = None  # Date string
    users_id: Optional[List[int]] = None


@mcp.tool()
def get_entries_texts(
    term: Optional[str] = None,
    mode: Optional[EntryTextMode] = None,
    items: Optional[int] = None,
    filter: Optional[EntriesTextFilter] = None
) -> dict:
    """
    Get entry texts with search and filter options.
    Args:
        term (str, optional): Text to search for, max length 1000.
        mode (str, required): EntryTextMode.
        items (int, optional): Number of items to return, min 1, max 800.
        filter (dict, optional): Filter object with keys: billable, customers_id, day, projects_id, services_id, time_since, time_until, users_id.
    Returns:
        dict: Entry texts data.
    """
    params = {}
    if term is not None:
        params['term'] = term
    if mode is not None:
        params['mode'] = mode
    if items is not None:
        params['items'] = items
    if filter is not None:
        params['filter'] = filter.model_dump(exclude_none=True)
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.ENTRIES_TEXTS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

@mcp.tool()
def get_holidayscarry(year: Optional[int] = None, users_id: Optional[int] = None) -> dict:
    """
    Get holidays carry data.
    Args:
        year (int, optional): Year, min 2000, max 2037.
        users_id (int, optional): User ID, min 1.
    Returns:
        dict: Holidays carry data.
    """
    params = {}
    if year is not None:
        params['year'] = year
    if users_id is not None:
        params['users_id'] = users_id
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.HOLIDAYS_CARRY.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

@mcp.tool()
def get_overtimecarry(year: Optional[int] = None, users_id: Optional[int] = None) -> dict:
    """
    Get overtime carry data.
    Args:
        year (int, optional): Year, min 2000, max 2037.
        users_id (int, optional): User ID, min 1.
    Returns:
        dict: Overtime carry data.
    """
    params = {}
    if year is not None:
        params['year'] = year
    if users_id is not None:
        params['users_id'] = users_id
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.OVERTIME_CARRY.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

@mcp.tool()
def get_overtimereductions(users_id: Optional[list] = None) -> dict:
    """
    Get overtime reductions.
    Args:
        users_id (list, optional): List of user IDs (int), min 1, max 500.
    Returns:
        dict: Overtime reductions data.
    """
    params = {}
    if users_id is not None:
        params['users_id'] = users_id
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.OVERTIME_REDUCTIONS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

class ApiProjectsReportsV3_SortForIndex(str, Enum):
    customers_name = "customers_name"
    customers_name_desc = "-customers_name"
    projects_name = "projects_name"
    projects_name_desc = "-projects_name"

class ProjectsReportsFilter(BaseModel):
    active: Optional[bool] = None
    fulltext: Optional[str] = None
    budget_source: Optional[List[BudgetSource]] = None


@mcp.tool()
def get_projects_reports(
    filter: Optional[ProjectsReportsFilter] = None,
    sort: Optional[List[ApiProjectsReportsV3_SortForIndex]] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get project reports with optional filtering, sorting, and paging.
    Args:
        filter (dict, optional): Filter object
        sort (list, optional): List of ApiProjectsReportsV3_SortForIndex.
        page (int, optional): Page number, min 1.
        items_per_page (int, optional): Items per page, min 1, max 1000.
    Returns:
        dict: Project reports data.
    """
    params = {}
    if filter is not None:
        params['filter'] = filter.model_dump(exclude_none=True)
    if sort is not None:
        params['sort'] = [s.value for s in sort]
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.PROJECTS_REPORTS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()


class SubprojectsFilter(BaseModel):
    active: Optional[bool] = None
    completed: Optional[bool] = None
    fulltext: Optional[str] = None
    projects_id: Optional[int] = None


@mcp.tool()
def get_subprojects(
    filter: Optional[SubprojectsFilter] = None,
    sort: Optional[SortIdName] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get subprojects with optional filtering, sorting, and paging.
    Args:
        filter (dict, optional): Filter object.
        sort (str, optional): SortIdName.
        page (int, optional): Page number, min 1.
        items_per_page (int, optional): Items per page, min 1, max 5000.
    Returns:
        dict: Subprojects data.
    """
    params = {}
    if filter is not None:
        params['filter'] = filter.model_dump(exclude_none=True)
    if sort is not None:
        params['sort'] = sort
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.SUBPROJECTS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

class TeamsFilter(BaseModel):
    fulltext: Optional[str] = None

@mcp.tool()
def get_teams(
    filter: Optional[TeamsFilter] = None,
    scope: Optional[UserScope] = None,
    sort: Optional[List[SortIdName]] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get teams with optional filtering, sorting, and paging.
    Args:
        filter (dict, optional): Filter object.
        scope (str, optional): UserScope.
        sort (list, optional): List of SortIdName.
        page (int, optional): Page number, min 1.
        items_per_page (int, optional): Items per page, min 1, max 1000.
    Returns:
        dict: Teams data.
    """
    params = {}
    if filter is not None:
        params['filter'] = filter.model_dump(exclude_none=True)
    if scope is not None:
        params['scope'] = scope
    if sort is not None:
        params['sort'] = sort
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.TEAMS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

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


class UsersFilter(BaseModel):
    active: Optional[bool] = None
    fulltext: Optional[str] = None
    teams_id: Optional[List[Optional[int]]] = None
    
@mcp.tool()
def get_users_all(
    filter: Optional[UsersFilter] = None,
    scope: Optional[UserScope] = None,
    sort: Optional[List[ApiUsersV3_SortForIndex]] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get users with optional filtering, sorting, and paging.
    Args:
        filter (dict, optional): Filter object.
        scope (str, optional): UserScope.
        sort (list, optional): List of ApiUsersV3_SortForIndex.
        page (int, optional): Page number, min 1.
        items_per_page (int, optional): Items per page, min 1, max 1000.
    Returns:
        dict: Users data.
    """
    params = {}
    if filter is not None:
        params['filter'] = filter.model_dump(exclude_none=True)
    if scope is not None:
        params['scope'] = scope
    if sort is not None:
        params['sort'] = [s.value for s in sort]
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.USERS_ALL.value, headers=AUTH_HEADERS, params=params)
    return resp.json()


# Filter model for /v3/usersNonbusinessGroups
class UsersNonbusinessGroupsFilter(BaseModel):
    nonbusiness_groups_id: Optional[List[int]] = None
    users_id: Optional[List[int]] = None

@mcp.tool()
def get_users_nonbusinessgroups(
    filter: Optional[UsersNonbusinessGroupsFilter] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get users nonbusiness groups with optional filtering and paging.
    Args:
        filter (UsersNonbusinessGroupsFilter, optional): Filter object.
        page (int, optional): Page number, min 1.
        items_per_page (int, optional): Items per page, min 1, max 1000.
    Returns:
        dict: Users nonbusiness groups data.
    """
    params = {}
    if filter is not None:
        params['filter'] = filter.model_dump(exclude_none=True)
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.USERS_NONBUSINESS_GROUPS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

class AbsencesFilter(BaseModel):
    status: Optional[List[AbsenceStatus]] = None
    teams_id: Optional[List[Optional[int]]] = None
    type: Optional[List[AbsenceType]] = None
    users_active: Optional[bool] = None
    users_id: Optional[List[int]] = None
    year: Optional[List[int]] = None

@mcp.tool()
def get_absences(
    filter: Optional[AbsencesFilter] = None,
    scope: Optional[str] = None  # AbsenceScope, not imported here
) -> dict:
    """
    Get absences with optional filtering and scope.
    Args:
        filter (AbsencesFilter, optional): Filter object.
        scope (str, optional): AbsenceScope.
    Returns:
        dict: Absences data.
    """
    params = {}
    if filter is not None:
        params['filter'] = filter.model_dump(exclude_none=True)
    if scope is not None:
        params['scope'] = scope
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.ABSENCES.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

class LumpSumServicesFilter(BaseModel):
    active: Optional[bool] = None
    fulltext: Optional[str] = None

@mcp.tool()
def get_lumpsumservices(
    filter: Optional[LumpSumServicesFilter] = None,
    sort: Optional[List[SortIdNameActive]] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get lump sum services with optional filtering, sorting, and paging.
    Args:
        filter (LumpSumServicesFilter, optional): Filter object.
        sort (list, optional): List of SortIdNameActive.
        page (int, optional): Page number, min 1.
        items_per_page (int, optional): Items per page, min 1, max 5000.
    Returns:
        dict: Lump sum services data.
    """
    params = {}
    if filter is not None:
        params['filter'] = filter.model_dump(exclude_none=True)
    if sort is not None:
        params['sort'] = sort
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.LUMPSUM_SERVICES.value, headers=AUTH_HEADERS, params=params)
    return resp.json()


class ProjectsFilter(BaseModel):
    active: Optional[bool] = None
    completed: Optional[bool] = None
    customers_id: Optional[int] = None
    fulltext: Optional[str] = None

@mcp.tool()
def get_projects(
    filter: Optional[ProjectsFilter] = None,
    sort: Optional[List[SortIdNameActive]] = None,
    scope: Optional[CustomerProjectScope] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get projects with optional filtering, sorting, and paging.
    Args:
        filter (ProjectsFilter, optional): Filter object.
        sort (list, optional): List of SortIdNameActive.
        scope (str, optional): CustomerProjectScope.
        page (int, optional): Page number, min 1.
        items_per_page (int, optional): Items per page, min 1, max 5000.
    Returns:
        dict: Projects data.
    """
    params = {}
    if filter is not None:
        params['filter'] = filter.model_dump(exclude_none=True)
    if sort is not None:
        params['sort'] = sort
    if scope is not None:
        params['scope'] = scope
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.PROJECTS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()


# Sort enum for /v4/projects/reports
class ApiProjectsReportsV4_SortForIndex(str, Enum):
    customers_name = "customers_name"
    customers_name_desc = "-customers_name"
    projects_name = "projects_name"
    projects_name_desc = "-projects_name"

# Filter model for /v4/projects/reports
class ProjectsReportsV4Filter(BaseModel):
    active: Optional[bool] = None
    fulltext: Optional[str] = None
    budget_source: Optional[List[BudgetSource]] = None

@mcp.tool()
def get_projects_reports_v4(
    filter: Optional[ProjectsReportsV4Filter] = None,
    sort: Optional[List[ApiProjectsReportsV4_SortForIndex]] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get v4 project reports with optional filtering, sorting, and paging.
    Args:
        filter (ProjectsReportsV4Filter, optional): Filter object.
        sort (list, optional): List of ApiProjectsReportsV4_SortForIndex.
        page (int, optional): Page number, min 1.
        items_per_page (int, optional): Items per page, min 1, max 1000.
    Returns:
        dict: Project reports data.
    """
    params = {}
    if filter is not None:
        params['filter'] = filter.model_dump(exclude_none=True)
    if sort is not None:
        params['sort'] = [s.value for s in sort]
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.PROJECTS_REPORTS_V4.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

class ServicesFilter(BaseModel):
    active: Optional[bool] = None
    fulltext: Optional[str] = None

@mcp.tool()
def get_services(
    filter: Optional[ServicesFilter] = None,
    sort: Optional[List[SortIdNameActive]] = None,
    scope: Optional[ServiceScope] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get services with optional filtering, sorting, and paging.
    Args:
        filter (ServicesFilter, optional): Filter object.
        sort (list, optional): List of SortIdNameActive.
        scope (str, optional): ServiceScope.
        page (int, optional): Page number, min 1.
        items_per_page (int, optional): Items per page, min 1, max 5000.
    Returns:
        dict: Services data.
    """
    params = {}
    if filter is not None:
        params['filter'] = filter.model_dump(exclude_none=True)
    if sort is not None:
        params['sort'] = sort
    if scope is not None:
        params['scope'] = scope
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.SERVICES.value, headers=AUTH_HEADERS, params=params)
    return resp.json()
