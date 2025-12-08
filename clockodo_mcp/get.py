""" get with ID endpoint mapping for clockodo_mcp """

from enum import Enum
from typing import Optional

from pydantic import BaseModel
import requests
from clockodo_mcp.clockodo_mcp import AUTH_HEADERS, mcp, BASE_URL

from clockodo_mcp.models import (
    AbsenceStatus, AbsenceType, Billable, BudgetSource, UserScope, UserReportType, CustomerProjectScope, EntryTextMode, ServiceScope, SortIdName, SortIdNameActive
)
from clockodo_mcp.utils import ApiProjectsReportsV4_SortForIndex, ApiUsersV3_SortForIndex, CustomerFilter, EntriesTextFilter, LumpSumServicesFilter, ProjectsFilter, ProjectsReportsV4Filter, ServiceEnum, ServiceEnumListAuto, ServicesFilter, UsersFilter, UsersNonbusinessGroupsFilter, flatten_dict, id_endpoint_map, noid_endpoint_map



class ServicGetList(Enum):
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


@mcp.tool()
def get_all(service: ServicGetList) -> dict:
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
    """
    endpoint_template = id_endpoint_map.get(ServiceEnum.userreports)
    endpoint = endpoint_template.format(id=id)
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params={"year": year, "type": type.value})
    return resp.json()

@mcp.tool()
def get_nonbusinessdays(id: int, year: Optional[int]) -> dict:
    """
    Get nonbusinessdays by ID and optional year.
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
    """
    endpoint_template = id_endpoint_map.get(ServiceEnum.users)
    endpoint = endpoint_template.format(id=id)
    params = {}
    if scope is not None:
        params["scope"] = scope.value
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=params)
    return resp.json()



# --- AUTO-GENERATED TOOLS FOR PARAMETERIZED ENDPOINTS ---

@mcp.tool()
def get_customers(
    filter: Optional[CustomerFilter] = None,
    sort: Optional[list[SortIdNameActive]] = None,
    scope: Optional[CustomerProjectScope] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get customers with optional filtering, sorting, and paging.
    """
    params = {}
    if filter is not None:
        filter_dict = filter.model_dump(exclude_none=True)
        params.update(flatten_dict(filter_dict, parent_key='filter'))
    if sort is not None:
        params['sort'] = [s.value for s in sort]
    if scope is not None:
        params['scope'] = scope.value
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.CUSTOMERS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

@mcp.tool()
def get_customers_count_projects(
    customers_id: Optional[list[int]] = None,
    scope: Optional[CustomerProjectScope] = None
) -> dict:
    """
    Get customer project counts.
    """
    params = {}
    if customers_id is not None:
        params['customers_id'] = customers_id
    if scope is not None:
        params['scope'] = scope.value
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.CUSTOMERS_COUNT_PROJECTS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()


@mcp.tool()
def get_entries_texts(
    term: Optional[str] = None,
    mode: Optional[EntryTextMode] = None,
    items: Optional[int] = None,
    filter: Optional[EntriesTextFilter] = None
) -> dict:
    """
    Get entry texts with search and filter options.
    """
    params = {}
    if term is not None:
        params['term'] = term
    if mode is not None:
        params['mode'] = mode.value
    if items is not None:
        params['items'] = items
    if filter is not None:
        filter_dict = filter.model_dump(exclude_none=True)
        params.update(flatten_dict(filter_dict, parent_key='filter'))
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.ENTRIES_TEXTS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

@mcp.tool()
def get_holidayscarry(year: Optional[int] = None, users_id: Optional[int] = None) -> dict:
    """
    Get holidays carry data.
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
    budget_source: Optional[list[BudgetSource]] = None


@mcp.tool()
def get_projects_reports(
    filter: Optional[ProjectsReportsFilter] = None,
    sort: Optional[list[ApiProjectsReportsV3_SortForIndex]] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get project reports with optional filtering, sorting, and paging.
    """
    params = {}
    if filter is not None:
        filter_dict = filter.model_dump(exclude_none=True)
        params.update(flatten_dict(filter_dict, parent_key='filter'))
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
    """
    params = {}
    if filter is not None:
        filter_dict = filter.model_dump(exclude_none=True)
        params.update(flatten_dict(filter_dict, parent_key='filter'))
    if sort is not None:
        params['sort'] = sort.value
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
    sort: Optional[list[SortIdName]] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get teams with optional filtering, sorting, and paging.
    """
    params = {}
    if filter is not None:
        filter_dict = filter.model_dump(exclude_none=True)
        params.update(flatten_dict(filter_dict, parent_key='filter'))
    if scope is not None:
        params['scope'] = scope.value
    if sort is not None:
        params['sort'] = sort
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.TEAMS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

    
@mcp.tool()
def get_users_all(
    filter: Optional[UsersFilter] = None,
    scope: Optional[UserScope] = None,
    sort: Optional[list[ApiUsersV3_SortForIndex]] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get users with optional filtering, sorting, and paging.
    """
    params = {}
    if filter is not None:
        filter_dict = filter.model_dump(exclude_none=True)
        params.update(flatten_dict(filter_dict, parent_key='filter'))
    if scope is not None:
        params['scope'] = scope.value
    if sort is not None:
        params['sort'] = [s.value for s in sort]
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    # Build the request object to get the final URL
    req = requests.Request(
        "GET",
        url=BASE_URL + ServiceEnumListAuto.USERS_ALL.value,
        headers=AUTH_HEADERS,
        params=params
    )
    prepped = req.prepare()
    # TODO: remove
    #with open("debug.txt", "w") as f:
    #    f.write(prepped.url + "\n")
    resp = requests.Session().send(prepped)
    return resp.json()


@mcp.tool()
def get_users_nonbusinessgroups(
    filter: Optional[UsersNonbusinessGroupsFilter] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get users nonbusiness groups with optional filtering and paging.
    """
    params = {}
    if filter is not None:
        filter_dict = filter.model_dump(exclude_none=True)
        params.update(flatten_dict(filter_dict, parent_key='filter'))
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.USERS_NONBUSINESS_GROUPS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()

class AbsencesFilter(BaseModel):
    status: Optional[list[AbsenceStatus]] = None
    teams_id: Optional[list[Optional[int]]] = None
    type: Optional[list[AbsenceType]] = None
    users_active: Optional[bool] = None
    users_id: Optional[list[int]] = None
    year: Optional[list[int]] = None

@mcp.tool()
def get_absences(
    filter: Optional[AbsencesFilter] = None,
    scope: Optional[str] = None  # AbsenceScope, not imported here
) -> dict:
    """
    Get absences with optional filtering and scope.
    """
    params = {}
    if filter is not None:
        filter_dict = filter.model_dump(exclude_none=True)
        params.update(flatten_dict(filter_dict))
    if scope is not None:
        params['scope'] = scope.value
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.ABSENCES.value, headers=AUTH_HEADERS, params=params)
    return resp.json()


@mcp.tool()
def get_lumpsumservices(
    filter: Optional[LumpSumServicesFilter] = None,
    sort: Optional[list[SortIdNameActive]] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get lump sum services with optional filtering, sorting, and paging.
    """
    params = {}
    if filter is not None:
        filter_dict = filter.model_dump(exclude_none=True)
        params.update(flatten_dict(filter_dict, parent_key='filter'))
    if sort is not None:
        params['sort'] = sort
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.LUMPSUM_SERVICES.value, headers=AUTH_HEADERS, params=params)
    return resp.json()


@mcp.tool()
def get_projects(
    filter: Optional[ProjectsFilter] = None,
    sort: Optional[list[SortIdNameActive]] = None,
    scope: Optional[CustomerProjectScope] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get projects with optional filtering, sorting, and paging.
    """
    params = {}
    if filter is not None:
        filter_dict = filter.model_dump(exclude_none=True)
        params.update(flatten_dict(filter_dict, parent_key='filter'))
    if sort is not None:
        params['sort'] = sort
    if scope is not None:
        params['scope'] = scope.value
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.PROJECTS.value, headers=AUTH_HEADERS, params=params)
    return resp.json()



@mcp.tool()
def get_projects_reports_v4(
    filter: Optional[ProjectsReportsV4Filter] = None,
    sort: Optional[list[ApiProjectsReportsV4_SortForIndex]] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get v4 project reports with optional filtering, sorting, and paging.
    """
    params = {}
    if filter is not None:
        filter_dict = filter.model_dump(exclude_none=True)
        params.update(flatten_dict(filter_dict, parent_key='filter'))
    if sort is not None:
        params['sort'] = [s.value for s in sort]
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.PROJECTS_REPORTS_V4.value, headers=AUTH_HEADERS, params=params)
    return resp.json()


@mcp.tool()
def get_services(
    filter: Optional[ServicesFilter] = None,
    sort: Optional[list[SortIdNameActive]] = None,
    scope: Optional[ServiceScope] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get services with optional filtering, sorting, and paging.
    """
    params = {}
    if filter is not None:
        filter_dict = filter.model_dump(exclude_none=True)
        params.update(flatten_dict(filter_dict, parent_key='filter'))
    if sort is not None:
        params['sort'] = sort
    if scope is not None:
        params['scope'] = scope.value
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + ServiceEnumListAuto.SERVICES.value, headers=AUTH_HEADERS, params=params)
    return resp.json()
