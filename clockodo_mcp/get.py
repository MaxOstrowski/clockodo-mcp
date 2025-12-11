""" get with ID endpoint mapping for clockodo_mcp """

from enum import Enum
from typing import Optional

from pydantic import BaseModel
import requests
from clockodo_mcp.clockodo_mcp import AUTH_HEADERS, mcp, BASE_URL

from clockodo_mcp.models import AbsenceScope, BillableDistinct, BudgetOption, ChangeRequestStatus, Grouping, UserScope, UserReportType, CustomerProjectScope, EntryTextMode, ServiceScope, SortIdName, SortIdNameActive
from clockodo_mcp.utils import TeamsFilter, AbsencesFilter, ApiProjectsReports_SortForIndex, ApiUsersV3_SortForIndex, CustomerFilter, EntriesTextFilter, LumpSumServicesFilter, ProjectsFilter, ProjectsReportsFilter, Service, ServicesFilter, SubprojectsFilter, UsersFilter, UsersNonbusinessGroupsFilter, flatten_dict, flatten_list, id_endpoint_map, noid_endpoint_map



class ServicGetList(Enum):
    targethours = Service.targethours.value
    userreports = Service.userreports.value
    accessgroups = Service.accessgroups.value
    clock = Service.clock.value
    holidaysquota = Service.holidaysquota.value
    nonbusinessdays = Service.nonbusinessdays.value
    nonbusinessgroups = Service.nonbusinessgroups.value
    customers = Service.customers.value
    holidayscarry = Service.holidayscarry.value
    overtimecarry = Service.overtimecarry.value
    overtimereductions = Service.overtimereductions.value
    subprojects = Service.subprojects.value
    teams = Service.teams.value
    users = Service.users.value
    usersnonbusinessgroups = Service.usersnonbusinessgroups.value
    absences = Service.absences.value
    lumpsumservices = Service.lumpsumservices.value
    projects = Service.projects.value
    services = Service.services.value


@mcp.tool()
def get_all(service: ServicGetList) -> dict:
    """ Get all entities for a given service """
    endpoint = noid_endpoint_map.get(Service(service.value))
    if not endpoint:
        raise ValueError(f"No endpoint mapping found for service: {service.value}")
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS)
    return resp.json()


class ServiceGetById(Enum):
    """ Services available for get by ID endpoint """
    targethours = Service.targethours.value
    accessgroups = Service.accessgroups.value
    entries = Service.entries.value
    holidaysquota = Service.holidaysquota.value
    nonbusinessdays = Service.nonbusinessdays.value
    nonbusinessgroups = Service.nonbusinessgroups.value
    customers = Service.customers.value
    holidayscarry = Service.holidayscarry.value
    overtimecarry = Service.overtimecarry.value
    overtimereductions = Service.overtimereductions.value
    subprojects = Service.subprojects.value
    teams = Service.teams.value
    users = Service.users.value
    usersnonbusinessgroups = Service.usersnonbusinessgroups.value
    absences = Service.absences.value
    lumpsumservices = Service.lumpsumservices.value
    projects = Service.projects.value
    services = Service.services.value


@mcp.tool()
def get(id: int, service: ServiceGetById) -> dict:
    """ Get entity by ID """
    endpoint_template = id_endpoint_map.get(Service(service.value))
    if not endpoint_template:
        raise ValueError(f"No endpoint mapping found for service: {service.value}")
    endpoint = endpoint_template.format(id=id)
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS)
    return resp.json()

# manually written get functions for services with special parameters

class EntriesFilter(BaseModel):
    users_id: Optional[int] = None
    customers_id: Optional[int] = None
    projects_id: Optional[int] = None
    subprojects_id: Optional[int] = None
    services_id: Optional[int] = None
    lumpsum_services_id: Optional[int] = None
    billable: Optional[BillableDistinct] = None
    texts_id: Optional[int] = None
    text: Optional[str] = None
    budget_type: Optional[BudgetOption] = None

@mcp.tool()
def get_entries(
    time_since: str,
    time_until: str,
    calc_also_revenues_for_projects_with_hard_budget: Optional[bool] = None,
    enhanced_list: Optional[bool] = None,
    filter: Optional[EntriesFilter] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get entries (time entries) for a given time range and optional filters.
    Parameters:
        time_since: Start datetime (required)
        time_until: End datetime (required)
        calc_also_revenues_for_projects_with_hard_budget: Optional boolean
        enhanced_list: Optional boolean
        filter: Optional EntriesFilter model
        page: Optional page number
        items_per_page: Optional items per page
    """
    params = {
        "time_since": time_since,
        "time_until": time_until,
    }
    if calc_also_revenues_for_projects_with_hard_budget is not None:
        params["calc_also_revenues_for_projects_with_hard_budget"] = calc_also_revenues_for_projects_with_hard_budget
    if enhanced_list is not None:
        params["enhanced_list"] = enhanced_list
    if filter is not None:
        filter_dict = filter.model_dump(exclude_none=True)
        params["filter"] = flatten_dict(filter_dict, parent_key="filter")
    if page is not None:
        params["page"] = page
    if items_per_page is not None:
        params["items_per_page"] = items_per_page
    endpoint = noid_endpoint_map.get(Service.entries)
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


class EntryGroupsFilter(BaseModel):
    """

    billable:
        NotBillable = 0
        Billable = 1
        Billed = 2

    """
    users_id: Optional[int] = None
    teams_id: Optional[int] = None
    customers_id: Optional[int] = None
    projects_id: Optional[int] = None
    subprojects_id: Optional[int] = None
    services_id: Optional[int] = None
    lumpsum_services_id: Optional[int] = None
    billable: Optional[BillableDistinct] = None  # Could be an enum if BillableDistinct is defined
    texts_id: Optional[int] = None
    text: Optional[str] = None
    budget_type: Optional[BudgetOption] = None  # Could be an enum if BudgetOption is defined


@mcp.tool()
def get_entrygroups(
    time_since: str,
    time_until: str,
    grouping: list[Grouping],
    round_to_minutes: Optional[int] = None,
    prepend_customer_to_project_name: Optional[bool] = None,
    calc_also_revenues_for_projects_with_hard_budget: Optional[bool] = None,
    filter: Optional[EntryGroupsFilter] = None
) -> dict:
    """
    Get entry groups (aggregated time entries) for a given time range and grouping.
    Parameters:
        time_since: Start datetime, Example: 2023-02-28T12:00:00Z
        time_until: End datetime, Example: 2023-03-28T12:00:00Z
        grouping: List of grouping criteria
        round_to_minutes: Rounding
        prepend_customer_to_project_name
        calc_also_revenues_for_projects_with_hard_budget
        filter (dict, optional): Filtering options
    """
    # Build params as a dict, flatten at the end for requests
    params = {
        "time_since": time_since,
        "time_until": time_until,
        "grouping": [group.value for group in grouping],
    }
    if round_to_minutes is not None:
        params["round_to_minutes"] = round_to_minutes
    if prepend_customer_to_project_name is not None:
        params["prepend_customer_to_project_name"] = prepend_customer_to_project_name
    if calc_also_revenues_for_projects_with_hard_budget is not None:
        params["calc_also_revenues_for_projects_with_hard_budget"] = calc_also_revenues_for_projects_with_hard_budget
    if filter is not None:
        params["filter"] = filter.model_dump(exclude_none=True)
    endpoint = noid_endpoint_map.get(Service.entrygroups)
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


@mcp.tool("restricted")
def get_worktimeschangerequests(
    date_since: Optional[str] = None,
    date_until: Optional[str] = None,
    users_id: Optional[int] = None,
    status: Optional[ChangeRequestStatus] = None,
    scope: Optional[str] = None,
    teams_id: Optional[list[int]] = None
) -> dict:
    """
    Get worktimes change requests with optional filters.
    Returns a list of change requests, only if a change request has been created before.
    """
    params = {}
    if date_since is not None:
        params["date_since"] = date_since
    if date_until is not None:
        params["date_until"] = date_until
    if users_id is not None:
        params["users_id"] = users_id
    if status is not None:
        params["status"] = status
    if scope is not None:
        params["scope"] = scope
    if teams_id is not None:
        params["teams_id"] = teams_id
    endpoint = noid_endpoint_map.get(Service.worktimeschangerequest)
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


@mcp.tool()
def get_userreports(id: int, year: int, type: Optional[UserReportType]) -> dict:
    """
    Get userreport by ID, year, and type.
    """
    endpoint_template = id_endpoint_map.get(Service.userreports)
    endpoint = endpoint_template.format(id=id)
    params = {
        "year": year,
    }
    if type is not None:
        params["type"] = type.value
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


@mcp.tool()
def get_nonbusinessdays(id: int, year: Optional[int]) -> dict:
    """
    Get nonbusinessdays by ID and optional year.
    """
    endpoint_template = id_endpoint_map.get(Service.nonbusinessdays)
    endpoint = endpoint_template.format(id=id)
    params = {}
    if year is not None:
        params["year"] = year
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()



@mcp.tool()
def get_users(id: int, scope: Optional[UserScope]) -> dict:
    """
    Get user by ID and optional scope.
    """
    endpoint_template = id_endpoint_map.get(Service.users)
    endpoint = endpoint_template.format(id=id)
    params = {}
    if scope is not None:
        params["scope"] = scope.value
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()



@mcp.tool()
def get_worktimes(users_id: int, date_since: str, date_until: str) -> dict:
    """
    Get worktimes by user ID and date range.
    example date: '2023-01-01'
    """
    endpoint = noid_endpoint_map.get(Service.worktimes)
    params = {
        "users_id": users_id,
        "date_since": date_since,
        "date_until": date_until
    }
    resp = requests.request("GET", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


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
        params['filter'] = filter
    if sort is not None:
        params['sort'] = sort
    if scope is not None:
        params['scope'] = scope.value
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.customers], headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


@mcp.tool("restricted")
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
        params['scope'] = scope
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.customers_count_projects], headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


@mcp.tool()
def get_entries_texts(
    mode: EntryTextMode,
    term: Optional[str] = None,
    items: Optional[int] = None,
    filter: Optional[EntriesTextFilter] = None
) -> dict:
    """
    Get entry texts with search and filter options.
    This only returns entries if additional notes are present.
    """
    params = {}
    if term is not None:
        params['term'] = term
    if mode is not None:
        params['mode'] = mode
    if items is not None:
        params['items'] = items
    if filter is not None:
        params['filter'] = filter
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.entries_texts], headers=AUTH_HEADERS, params=flatten_dict(params))
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
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.holidayscarry], headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


@mcp.tool("restricted")
def get_overtimecarry(year: Optional[int] = None, users_id: Optional[int] = None) -> dict:
    """
    Get overtime carry data.
    """
    params = {}
    if year is not None:
        params['year'] = year
    if users_id is not None:
        params['users_id'] = users_id
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.overtimecarry], headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


@mcp.tool("restricted")
def get_overtimereductions(users_id: Optional[list] = None) -> dict:
    """
    Get overtime reductions.
    """
    params = {}
    if users_id is not None:
        params['users_id'] = users_id
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.overtimereductions], headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


@mcp.tool()
def get_projects_reports(
    filter: Optional[ProjectsReportsFilter] = None,
    sort: Optional[list[ApiProjectsReports_SortForIndex]] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get project reports with optional filtering, sorting, and paging.
    """
    params = {}
    if filter is not None:
        params['filter'] = filter
    if sort is not None:
        params['sort'] = sort
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.projects_reports], headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


@mcp.tool()
def get_subprojects(
    filter: Optional[SubprojectsFilter] = None,
    sort: Optional[SortIdName] = None,
    page: Optional[int] = None,
    items_per_page: Optional[int] = None
) -> dict:
    """
    Get subprojects with optional filtering, sorting, and paging.
    sort parameter might be broken?
    """
    params = {}
    if filter is not None:
        params['filter'] = filter
    if sort is not None:
        params['sort'] = sort
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.subprojects], headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


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
        params['filter'] = filter
    if scope is not None:
        params['scope'] = scope.value
    if sort is not None:
        params['sort'] = sort
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.teams], headers=AUTH_HEADERS, params=flatten_dict(params))
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
        params['filter'] = filter
    if scope is not None:
        params['scope'] = scope.value
    if sort is not None:
        params['sort'] = sort
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    # Build the request object to get the final URL
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.users], headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


@mcp.tool("restricted")
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
        params['filter'] = filter
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.usersnonbusinessgroups], headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


@mcp.tool()
def get_absences(
    filter: Optional[AbsencesFilter] = None,
    scope: Optional[AbsenceScope] = None
) -> dict:
    """
    Get absences with optional filtering and scope.
    """
    params = {}
    if filter is not None:
        params['filter'] = filter
    if scope is not None:
        params['scope'] = scope
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.absences], headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


@mcp.tool("restricted")
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
        params['filter'] = filter
    if sort is not None:
        params['sort'] = sort
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.lumpsumservices], headers=AUTH_HEADERS, params=flatten_dict(params))
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
        params['filter'] = filter
    if sort is not None:
        params['sort'] = sort
    if scope is not None:
        params['scope'] = scope
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.projects], headers=AUTH_HEADERS, params=flatten_dict(params))
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
        params['filter'] = filter
    if sort is not None:
        params['sort'] = sort
    if scope is not None:
        params['scope'] = scope
    if page is not None:
        params['page'] = page
    if items_per_page is not None:
        params['items_per_page'] = items_per_page
    resp = requests.request("GET", url=BASE_URL + noid_endpoint_map[Service.services], headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()
