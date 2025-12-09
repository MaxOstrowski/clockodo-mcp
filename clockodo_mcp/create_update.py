from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel, Field
from clockodo_mcp.clockodo_mcp import AUTH_HEADERS, BASE_URL, mcp
from clockodo_mcp.models import AbsenceStatus, AccessType, AccessValue, ApiAccessGroupsProjectsV2AccessValueForPut, ApiAccessGroupsServicesGeneralV2AccessTypeForPut, ApiAccessGroupsServicesV2AccessTypeForPut, ApiAccessGroupsServicesV2AccessValueForPut, Billable, BillableDistinct, BudgetOption, ChangeRequestIntervalType, CustomerColor, GeneralAccessV2, NonbusinessDayType, TargetHourType, Thresholds
from clockodo_mcp.utils import Service, flatten_dict, noid_endpoint_map, id_endpoint_map
import requests
from typing import Optional, Union

@mcp.tool()
def create_targethour(
	users_id: int,
	type: TargetHourType,
	date_since: str,
	date_until: str,
	compensation_monthly: float,
	monday: Optional[float] = None,
	tuesday: Optional[float] = None,
	wednesday: Optional[float] = None,
	thursday: Optional[float] = None,
	friday: Optional[float] = None,
	saturday: Optional[float] = None,
	sunday: Optional[float] = None,
	monthly_target: Optional[float] = None,
	workday_monday: Optional[bool] = None,
	workday_tuesday: Optional[bool] = None,
	workday_wednesday: Optional[bool] = None,
	workday_thursday: Optional[bool] = None,
	workday_friday: Optional[bool] = None,
	workday_saturday: Optional[bool] = None,
	workday_sunday: Optional[bool] = None,
	compensation_daily: Optional[float] = None,
	holiday_fixed_credit: Optional[int] = None,
	surcharge_models_id: Optional[int] = None
) -> dict:
	"""
	Create a targethour entry.

	Required parameters:
		users_id (int): User ID. Minimum: 1. Example: 42
		type (TargetHourType): TargetHourType. Example: "default"
		date_since (str): Start date (YYYY-MM-DD). Format: date. Example: "2023-02-28"
		date_until (str): End date (YYYY-MM-DD or null). Format: date. Example: "2023-03-31"
		compensation_monthly (float): Monthly compensation in minutes. Min: 0, Max: 744. Example: 160.0
		monday, tuesday, wednesday, thursday, friday, saturday, sunday (float):
			Target hours per day. Min: 0, Max: 24. Format: float. Example: 8.0
		monthly_target (float): Monthly target hours. Min: 0, Max: 744. Format: float. Example: 160.0
		workday_monday, workday_tuesday, workday_wednesday, workday_thursday, workday_friday, workday_saturday, workday_sunday (bool):
			Is workday. Example: True
		compensation_daily (float): Automatic time compensation per day in minutes. Min: 0, Max: 1440. Example: 30.0
		holiday_fixed_credit (int): Fixed holiday credit. Enum: [0, 1]. Example: 1
		surcharge_models_id (int): Surcharge model ID. Min: 1. Example: 5
	"""
	payload = {
		"users_id": users_id,
		"type": type.value,
		"date_since": date_since,
		"date_until": date_until,
		"compensation_monthly": compensation_monthly,
	}
	# Add optional fields if provided
	optional_fields = [
		"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",
		"monthly_target", "workday_monday", "workday_tuesday", "workday_wednesday",
		"workday_thursday", "workday_friday", "workday_saturday", "workday_sunday",
		"compensation_daily", "holiday_fixed_credit", "surcharge_models_id"
	]
	for field in optional_fields:
		value = locals()[field]
		if value is not None:
			payload[field] = value
	endpoint = noid_endpoint_map.get(Service.targethours)
	resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
	return resp.json()


@mcp.tool()
def update_targethour(
	id: int,
	type: TargetHourType,
	date_since: str,
	date_until: Optional[str] = None,
	monday: Optional[float] = None,
	tuesday: Optional[float] = None,
	wednesday: Optional[float] = None,
	thursday: Optional[float] = None,
	friday: Optional[float] = None,
	saturday: Optional[float] = None,
	sunday: Optional[float] = None,
	monthly_target: Optional[float] = None,
	workday_monday: Optional[bool] = None,
	workday_tuesday: Optional[bool] = None,
	workday_wednesday: Optional[bool] = None,
	workday_thursday: Optional[bool] = None,
	workday_friday: Optional[bool] = None,
	workday_saturday: Optional[bool] = None,
	workday_sunday: Optional[bool] = None,
	compensation_daily: Optional[float] = None,
	compensation_monthly: Optional[float] = None,
	holiday_fixed_credit: Optional[int] = None,
	surcharge_models_id: Optional[int] = None
) -> dict:
	"""
	Update a targethour entry.

	Required parameters:
		id (int): Targethour row ID. Example: 1
		type (TargetHourType): TargetHourType. Example: "default"
		date_since (str): Start date (YYYY-MM-DD). Format: date. Example: "2023-02-28"

	Optional parameters:
		date_until (str): End date (YYYY-MM-DD or null). Format: date. Example: "2023-03-31"
		monday, tuesday, wednesday, thursday, friday, saturday, sunday (float):
			Target hours per day. Min: 0, Max: 24. Format: float. Example: 8.0
		monthly_target (float): Monthly target hours. Min: 0, Max: 744. Format: float. Example: 160.0
		workday_monday, workday_tuesday, workday_wednesday, workday_thursday, workday_friday, workday_saturday, workday_sunday (bool):
			Is workday. Example: True
		compensation_daily (float): Compensation per day in minutes. Min: 0, Max: 1440. Example: 30.0
		compensation_monthly (float): Compensation per month in minutes. Min: 0, Max: 744. Example: 160.0
		holiday_fixed_credit (int): Fixed holiday credit. Enum: [0, 1]. E
		surcharge_models_id (int): Surcharge model ID. Min: 1. Example: 5
	"""
	payload = {
		"type": type.value,
		"date_since": date_since,
	}
	optional_fields = [
		"date_until", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",
		"monthly_target", "workday_monday", "workday_tuesday", "workday_wednesday",
		"workday_thursday", "workday_friday", "workday_saturday", "workday_sunday",
		"compensation_daily", "compensation_monthly", "holiday_fixed_credit", "surcharge_models_id"
	]
	for field in optional_fields:
		value = locals()[field]
		if value is not None:
			payload[field] = value
	endpoint = id_endpoint_map.get(Service.targethours).format(id=id)
	resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
	return resp.json()



class WorkTimesChangeRequestChange(BaseModel):
	type: ChangeRequestIntervalType = Field(..., description="1=Added, 2=Removed")
	time_since: str  # ISO 8601 datetime string
	time_until: str  # ISO 8601 datetime string


@mcp.tool()
def create_worktimeschangerequest(
	date: str,
	users_id: int,
	changes: list[WorkTimesChangeRequestChange],
) -> dict:
	"""
	Create a worktimes change request to modify work times for a user.
	After creation of the request, the worktime can be changed or deleted.

    date (str): Date for the change request. Format: YYYY-MM-DD. Example: "2023-02-28"
    users_id (int): User ID. Minimum: 1. Example: 42
    changes: List of change objects. Each object must include:
        type (str): ChangeRequestIntervalType
        time_since (str): Start time (ISO 8601). Example: "2023-02-28T12:00:00Z"
        time_until (str): End time (ISO 8601). Example: "2023-02-28T12:00:00Z"

	"""
	changes_flat = [flatten_dict(c.model_dump()) for c in changes]
	payload = {
		"date": date,
		"users_id": users_id,
		"changes": changes_flat,
	}
	endpoint = noid_endpoint_map.get(Service.worktimeschangerequest)
	resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
	return resp.json()


@mcp.tool()
def update_accessgroups_customer(
    accessGroupsId: int,
    type: AccessType,
    value: AccessValue,
    id: Optional[int] = None
) -> dict:
    """
    Update customer access for a specific access group. If id is provided, updates a specific customer; otherwise, updates general customer access.
    accessGroupsId (int): Access group ID
    type (AccessType): Access type
    value (AccessValue): Access value
    id (int, optional): Customer ID
    """
    payload = {
        "type": type.value,
        "value": value.value
    }
    if id is not None:
        payload["id"] = id
        endpoint = id_endpoint_map.get(Service.accessgroups_customers).format(id=accessGroupsId)
    else:
        endpoint = id_endpoint_map.get(Service.accessgroups_customers_general).format(id=accessGroupsId)
    resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def update_accessgroups_project(
    accessGroupsId: int,
    id: int,
    type: AccessType,
    value: ApiAccessGroupsProjectsV2AccessValueForPut
) -> dict:
    """
    Update project access for a specific access group.
    accessGroupsId (int): Access group ID
    id (int): Project ID
    type (str): AccessType
    value (str): ApiAccessGroupsProjectsV2_AccessValueForPut, Use 0 for no access. Use 1 for full access.
    """
    payload = {
        "id": id,
        "type": type.value,
        "value": value.value
    }
    endpoint = id_endpoint_map.get(Service.accessgroups_projects).format(id=accessGroupsId)
    resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def update_accessgroups_service(
    accessGroupsId: int,
    type: ApiAccessGroupsServicesV2AccessTypeForPut,
    value: ApiAccessGroupsServicesV2AccessValueForPut,
	id: Optional[int],
) -> dict:
    """
    Update service access for a specific access group. If id is provided, updates a specific service; otherwise, updates general service access.
    accessGroupsId (int): Access group ID
    id (int): Service ID
    type (str): ApiAccessGroupsServicesV2_AccessTypeForPut
    value (str): ApiAccessGroupsServicesV2_AccessValueForPut, Use 0 for no access. Use 1 for full access.
    """
    payload = {
        "type": type.value,
        "value": value.value,
    }
    if id is not None:
        payload["id"] = id
        endpoint = id_endpoint_map.get(Service.accessgroups_services).format(id=accessGroupsId)
    else:
        endpoint = id_endpoint_map.get(Service.accessgroups_services_general).format(id=accessGroupsId)
    resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def create_accessgroup(
    name: str,
    users_ids: Optional[list[int]] = None
) -> dict:
    """
    Create a new access group.
    name (str): Name of the access group (max 100 chars)
    users_ids: IDs of group members
    """
    payload = {"name": name}
    if users_ids is not None:
        payload["users_ids"] = users_ids
    endpoint = noid_endpoint_map.get(Service.accessgroups)
    resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def create_clock(
    customers_id: int,
    services_id: int,
    billable: Optional[Billable] = None,
    duration_transfer: Optional[int] = None,
    projects_id: Optional[int] = None,
    subprojects_id: Optional[int] = None,
    text: Optional[str] = None,
    time_since: Optional[str] = None,
    users_id: Optional[int] = None
) -> dict:
    """
    Start a clock (begin a time entry).
    customers_id (int): Customer ID
    services_id (int): Service ID
    billable (int, optional): Billable status
    duration_transfer (int, optional): Duration transfer
    projects_id (int, optional): Project ID
    subprojects_id (int, optional): Subproject ID
    text (str, optional): Entry text (max 1000 chars)
    time_since (str, optional): Start time (ISO 8601)
    users_id (int, optional): User ID
    """
    payload = {
        "customers_id": customers_id,
        "services_id": services_id
    }
    if billable is not None:
        payload["billable"] = billable.value
    if duration_transfer is not None:
        payload["duration_transfer"] = duration_transfer
    if projects_id is not None:
        payload["projects_id"] = projects_id
    if subprojects_id is not None:
        payload["subprojects_id"] = subprojects_id
    if text is not None:
        payload["text"] = text
    if time_since is not None:
        payload["time_since"] = time_since
    if users_id is not None:
        payload["users_id"] = users_id
    endpoint = noid_endpoint_map.get(Service.clock)
    resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def update_clock(
    id: int,
    time_since: Optional[str] = None,
    time_since_before: Optional[str] = None,
    time_until_before: Optional[str] = None,
    duration: Optional[int] = None,
    duration_before: Optional[int] = None
) -> dict:
    """
    Change duration of a clock entry.
    id (int): Clock entry ID
    time_since (str, optional): New start time (ISO 8601)
    time_since_before (str, optional): Previous start time (ISO 8601)
    time_until_before (str, optional): Previous end time (ISO 8601)
    duration (int, optional): New duration
    duration_before (int, optional): Previous duration
    """
    payload = {}
    if time_since is not None:
        payload["time_since"] = time_since
    if time_since_before is not None:
        payload["time_since_before"] = time_since_before
    if time_until_before is not None:
        payload["time_until_before"] = time_until_before
    if duration is not None:
        payload["duration"] = duration
    if duration_before is not None:
        payload["duration_before"] = duration_before
    endpoint = id_endpoint_map.get(Service.clock).format(id=id)
    resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def create_or_update_entry(
    customers_id: Optional[int] = None,
    services_id: Optional[int] = None,
    users_id: Optional[int] = None,
    time_since: Optional[str] = None,
    time_until: Optional[str] = None,
    text: Optional[str] = None,
    billable: Optional[bool] = None,
    projects_id: Optional[int] = None,
    subprojects_id: Optional[int] = None,
    lump_sum_services_id: Optional[int] = None,
    pause_duration: Optional[int] = None,
    is_clocked: Optional[bool] = None,
    clocked_since: Optional[str] = None,
    clocked_until: Optional[str] = None,
    id: Optional[int] = None
) -> dict:
    """
    Create or update an entry in Clockodo MCP.
    If id is provided, updates the entry
    If id is not provided, creates a new entry 
    """
    payload = {
        "customers_id": customers_id,
        "services_id": services_id,
        "users_id": users_id,
        "time_since": time_since,
        "time_until": time_until,
        "text": text,
        "billable": billable,
        "projects_id": projects_id,
        "subprojects_id": subprojects_id,
        "lump_sum_services_id": lump_sum_services_id,
        "pause_duration": pause_duration,
        "is_clocked": is_clocked,
        "clocked_since": clocked_since,
        "clocked_until": clocked_until
    }
    if id is not None:
        endpoint = id_endpoint_map.get(Service.entries).format(id=id)
        resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        endpoint = noid_endpoint_map.get(Service.entries)
        resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


class EntryGroupFilter(BaseModel):
    users_id: Optional[int] = None
    teams_id: Optional[int] = None
    customers_id: Optional[int] = None
    projects_id: Optional[int] = None
    subprojects_id: Optional[int] = None
    services_id: Optional[int] = None
    lumpsum_services_id: Optional[int] = None
    billable: Optional[BillableDistinct] = None  # BillableDistinct
    texts_id: Optional[int] = None
    text: Optional[str] = None
    budget_type: Optional[BudgetOption] = None


@mcp.tool()
def update_entrygroup(
    time_since: str,
    time_until: str,
    users_id: Optional[int] = None,
    customers_id: Optional[int] = None,
    projects_id: Optional[int] = None,
    subprojects_id: Optional[int] = None,
    services_id: Optional[int] = None,
    lumpsum_services_id: Optional[int] = None,
    billable: Optional[BillableDistinct] = None,
    text: Optional[str] = None,
    hourly_rate: Optional[float] = None,
    confirm_key: Optional[str] = None,
    filter: Optional[EntryGroupFilter] = None
) -> dict:
    """
    Update entry groups in Clockodo MCP (bulk update).
    Update multiple entry groups at once, based on a time range and optional filters (user, project, billable status, etc.).
    Common use: Change properties (e.g., billable status, text, hourly rate) for all entries matching the filter and time range.
    time in format date-time, example: "2023-02-28T12:00:00Z"
    billable: 0=Non-billable, 1=Billable, 2=Billed
    confirmation_key: For safety, the api will respond with a confirmation key with which you have to request once again in order to confirm your edit action.
    """
    payload = {
        "time_since": time_since,
        "time_until": time_until
    }
    if users_id is not None:
        payload["users_id"] = users_id
    if customers_id is not None:
        payload["customers_id"] = customers_id
    if projects_id is not None:
        payload["projects_id"] = projects_id
    if subprojects_id is not None:
        payload["subprojects_id"] = subprojects_id
    if services_id is not None:
        payload["services_id"] = services_id
    if lumpsum_services_id is not None:
        payload["lumpsum_services_id"] = lumpsum_services_id
    if billable is not None:
        payload["billable"] = billable.value
    if text is not None:
        payload["text"] = text
    if hourly_rate is not None:
        payload["hourly_rate"] = hourly_rate
    if confirm_key is not None:
        payload["confirm_key"] = confirm_key
    if filter is not None:
        payload["filter"] = flatten_dict(filter.model_dump())
    endpoint = noid_endpoint_map.get(Service.entrygroups)
    resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def create_or_update_holiday_quota(
    users_id: Optional[int] = None,
    year_since: Optional[int] = None,
    year_until: Optional[int] = None,
    count: Optional[float] = None,
    note: Optional[str] = None,
    id: Optional[int] = None
) -> dict:
    """
    Create or update a holiday quota in Clockodo MCP.
    If id is provided, updates the quota
    If id is not provided, creates a new quota
    year is of form YYYY, example: 2023
    """
    payload = {}
    if users_id is not None:
        payload["users_id"] = users_id
    if year_since is not None:
        payload["year_since"] = year_since
    if year_until is not None:
        payload["year_until"] = year_until
    if count is not None:
        payload["count"] = count
    if note is not None:
        payload["note"] = note
    if id is not None:
        endpoint = id_endpoint_map.get(Service.holidaysquota).format(id=id)
        resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        endpoint = noid_endpoint_map.get(Service.holidaysquota)
        resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def clear_individual_user_access(users_id: int) -> dict:
    """
    Clear all individual user access for the specified user.
    """
    endpoint = id_endpoint_map.get(Service.individualuseraccess_users_clear).format(id=users_id)
    resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS)
    return resp.json()


class IndividualUserAccessType(Enum):
    PROJECT = "project"
    SERVICE = "service"
    SERVICE_GENERAL = "service_general"


@mcp.tool()
def update_individual_user_access(
    access_type: IndividualUserAccessType,
    users_id: int,
    type: AccessType,
    value: AccessValue,
    id: Optional[int] = None
) -> dict:
    """
    Update individual user access for a project, service, or general service.
    users_id (int): User ID
    id (int, optional): Project or Service ID (not required for service_general)
    type: only add allowed for service and service_general
    """
    payload = {"value": value.value}
    if access_type == IndividualUserAccessType.PROJECT:
        endpoint = id_endpoint_map.get(Service.individualuseraccess_users_projects).format(id=users_id)
        payload["id"] = id
    elif access_type == IndividualUserAccessType.SERVICE:
        endpoint = id_endpoint_map.get(Service.individualuseraccess_users_services).format(id=users_id)
        payload["id"] = id
    elif access_type == IndividualUserAccessType.SERVICE_GENERAL:
        endpoint = id_endpoint_map.get(Service.individualuseraccess_users_services_general).format(id=users_id)
    else:
        raise ValueError("Invalid access_type")
    resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def create_or_update_nonbusiness_day(
    nonbusiness_group_id: int,
    type: NonbusinessDayType,
    name: str,
    half_day: bool,
    surcharge_special: bool,
    evaluated_date: str,
    special_id: Optional[int] = None,
    day: Optional[int] = None,
    month: Optional[int] = None,
    year: Optional[int] = None,
    id: Optional[int] = None
) -> dict:
    """
    Create or update a nonbusiness day.
    If id is provided, updates the nonbusiness day
    If id is not provided, creates a new nonbusiness day
    """
    payload = {
        "nonbusiness_group_id": nonbusiness_group_id,
        "type": type.value,
        "name": name,
        "half_day": half_day,
        "surcharge_special": surcharge_special,
        "evaluated_date": evaluated_date
    }
    if special_id is not None:
        payload["special_id"] = special_id
    if day is not None:
        payload["day"] = day
    if month is not None:
        payload["month"] = month
    if year is not None:
        payload["year"] = year

    if id is not None:
        endpoint = id_endpoint_map.get(Service.nonbusinessdays).format(id=id)
        resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        endpoint = noid_endpoint_map.get(Service.nonbusinessdays)
        resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def create_or_update_nonbusiness_group(
    name: str,
    company_default: bool,
    id: Optional[int] = None
) -> dict:
    """
    Create or update a nonbusiness group.
    If id is provided, updates the nonbusiness group (PUT).
    If id is not provided, creates a new nonbusiness group (POST).
    """
    payload = {
        "name": name,
        "company_default": company_default
    }
    if id is not None:
        endpoint = id_endpoint_map.get(Service.nonbusinessgroups).format(id=id)
        resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        payload["id"] = id
        endpoint = noid_endpoint_map.get(Service.nonbusinessgroups)
        resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


class CustomerProjectsAccess(BaseModel):
    projects: dict[str, bool]


@mcp.tool()
def create_or_update_customer_projects_access(
        users_id: int,
        access: dict[str, Union[bool, CustomerProjectsAccess]],
    ) -> dict:
    """
    Create or update customer-projects access for a user.
    access: Dict mapping customer IDs to either True (full access) or a dict with 'projects' mapping project IDs to True.
    Examples:
        access = {
            "123": True,  # Full access to customer 123
            "456": CustomerProjectsAccess(projects={"789": True, "101": True})  # Access to projects 789 and 101 of customer 456
        }
    If id is provided, updates the access. If not, creates new access.
    """
    payload = {}
    for name, access in access.items():
        if isinstance(access, bool):
            payload[name] = access
        elif isinstance(access, CustomerProjectsAccess):
            payload[name]  = flatten_dict(access.model_dump())
    if users_id is not None:
        endpoint = id_endpoint_map.get(Service.users_access_customers_projects).format(id=users_id)
        resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        endpoint = noid_endpoint_map.get(Service.users_access_customers_projects)
        resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()



@mcp.tool()
def create_or_update_service_access(
    users_id: int,
    add: Union[bool, dict[str, bool]],
    id: Optional[int] = None
) -> dict:
    """
    Create or update service access for a user.
    add: True for general access, or a dict mapping service IDs to True for specific access.
    Examples:
        add = True  # Full access to all services
        add = {"123": True, "456": True}  # Access to services 123 and 456 only
    If id is provided, updates the access. If not, creates new access.
    """
    payload = {"add": add}
    if id is not None:
        endpoint = id_endpoint_map.get(Service.users_access_services).format(id=id)
        resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        endpoint = noid_endpoint_map.get(Service.users_access_services)
        resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


from typing import Any


@mcp.tool()
def create_or_update_customer(
    name: str,
    number: Optional[str] = None,
    active: Optional[bool] = None,
    billable_default: Optional[bool] = None,
    note: Optional[str] = None,
    color: Optional[CustomerColor] = None,
    bill_service_id: Optional[str] = None,
    id: Optional[int] = None
) -> dict:
    """
    Create or update a customer (v3).
    If id is provided, updates the customer (PUT /v3/customers/{id}), else creates a new customer (POST /v3/customers).
    Fields:
      name: Customer name (required for create, max 100)
      number: Freely selectable number (max 50)
      active: Is customer active
      billable_default: Default billable
      note: Note (max 1000), Can only be set by owners or workers with elevated access `manage_customers_and_projects`
      color: Possible values:
              - `1`: BloodOrange
              - `2`: Sunflower
              - `3`: LightGreen
              - `4`: Caribbean
              - `5`: Sky
              - `6`: BrandBlue
              - `7`: BluePurple
              - `8`: Magenta
              - `9`: ChewingGum
      bill_service_id: Billing service id (max 50), Can only be set by owners or workers with elevated access `manage_customers_and_projects` and if a billing application with customers support is linked up
      id: Customer id for update, none for create
    """
    payload = {}
    if name is not None:
        payload["name"] = name
    if number is not None:
        payload["number"] = number
    if active is not None:
        payload["active"] = active
    if billable_default is not None:
        payload["billable_default"] = billable_default
    if note is not None:
        payload["note"] = note
    if color is not None:
        payload["color"] = color.value
    if bill_service_id is not None:
        payload["bill_service_id"] = bill_service_id
    if id is not None:
        endpoint = id_endpoint_map.get(Service.customers).format(id=id)
        resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        endpoint = noid_endpoint_map.get(Service.customers)
        resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def create_or_update_holidayscarry(
    year: int,
    count: float,
    note: Optional[str] = None,
    users_id: Optional[int] = None,
    id: Optional[int] = None
) -> dict:
    """
    Create or update a holiday carryover record (v3).
    If id is provided, updates the record, else user_id is needed to create a new record.
    Fields:
        year (int): Year for the carryover (2000-2037)
        count (float): Carryover amount, Only full and half values allowed, e.g. 4.0 or 4.5
        note (str, optional): Note (max 1000)
        id (int, optional): Record id for update
    """
    payload = {}
    if year is not None:
        payload["year"] = year
    if users_id is not None:
        payload["users_id"] = users_id
    if count is not None:
        payload["count"] = count
    if note is not None:
        payload["note"] = note
    if id is not None:
        endpoint = id_endpoint_map.get(Service.holidayscarry).format(id=id)
        resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        endpoint = noid_endpoint_map.get(Service.holidayscarry)
        resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def create_or_update_overtimecarry(
    year: int,
    count: float,
    note: Optional[str] = None,
    users_id: Optional[int] = None,
    id: Optional[int] = None
) -> dict:
    """
    Create or update an overtime carryover record (v3).
    If id is provided, updates the record, else users_id is needed to create a new record.
    Fields:
        year (int): Year for the carryover (2000-2037)
        count (float): Carryover amount, can be negative or positive
        note (str, optional): Note (max 1000)
        users_id (int, optional): User id for create
        id (int, optional): Record id for update
    """
    payload = {}
    if year is not None:
        payload["year"] = year
    if users_id is not None:
        payload["users_id"] = users_id
    if count is not None:
        payload["count"] = count
    if note is not None:
        payload["note"] = note
    if id is not None:
        endpoint = id_endpoint_map.get(Service.overtimecarry).format(id=id)
        resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        endpoint = noid_endpoint_map.get(Service.overtimecarry)
        resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def create_or_update_overtimereduction(
    users_id: Optional[int] = None,
    date: str = None,
    hours: float = None,
    note: Optional[str] = None,
    id: Optional[int] = None
) -> dict:
    """
    Create or update an overtime reduction record (v3).
    If id is provided, updates the record, else creates a new record.
    Fields:
        users_id: User ID (required for create)
        date: Date of reduction (YYYY-MM-DD, required for create/update)
        hours: Amount of hours reduced (required for create/update, -999 to 999)
        note: max 1000 characters
        id: Record id for update
    """
    payload = {}
    if users_id is not None:
        payload["users_id"] = users_id
    if date is not None:
        payload["date"] = date
    if hours is not None:
        payload["hours"] = hours
    if note is not None:
        payload["note"] = note
    if id is not None:
        endpoint = id_endpoint_map.get(Service.overtimereductions).format(id=id)
        resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        endpoint = noid_endpoint_map.get(Service.overtimereductions)
        resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()



from pydantic import BaseModel, Field


class SubprojectBudget(BaseModel):
    amount: Optional[float] = Field(
        None,
        description="Budget amount (float, -99999999.99 to 99999999.99)",
        ge=-99999999.99,
        le=99999999.99,
    )
    monetary: Optional[bool] = Field(
        None,
        description="Is the budget monetary?"
    )
    hard: Optional[bool] = Field(
        None,
        description="Is the budget hard?"
    )
    notification_thresholds: Optional[list[Thresholds]] = Field(
        None,
        description="List of notification thresholds (schema depends on Thresholds model) "
                    "Percent50 = 50, "
                    "Percent60 = 60, "
                    "Percent70 = 70, "
                    "Percent80 = 80, "
                    "Percent90 = 90, "
                    "Percent100 = 100, "
                    "Percent110 = 110, "
                    "Percent120 = 120, "
                    "Percent130 = 130, "
                    "Percent140 = 140, "
                    "Percent150 = 150, "
                    "Percent200 = 200, "
                    "Percent250 = 250, "
                    "Percent300 = 300"
    )


@mcp.tool()
def create_or_update_subproject(
    projects_id: Optional[int] = None,
    name: Optional[str] = None,
    billable_default: Optional[bool] = None,
    budget: Optional[SubprojectBudget] = None,
    number: Optional[str] = None,
    note: Optional[str] = None,
    start_date: Optional[str] = None,
    deadline: Optional[str] = None,
    bill_service_id: Optional[str] = None,
    id: Optional[int] = None
) -> dict:
    """
    Create or update a subproject (v3).
    If id is provided, updates the subproject else creates a new subproject.
    Fields:
        projects_id: Parent project ID (required for create)
        name: Subproject name (required)
        start_date: YYYY-MM-DD
        deadline: YYYY-MM-DD
        bill_service_id: Max 50 chars
        id: Subproject ID for update
    """
    payload = {}
    if projects_id is not None:
        payload["projects_id"] = projects_id
    if name is not None:
        payload["name"] = name
    if billable_default is not None:
        payload["billable_default"] = billable_default
    if budget is not None:
        payload["budget"] = flatten_dict(budget.model_dump())
    if number is not None:
        payload["number"] = number
    if note is not None:
        payload["note"] = note
    if start_date is not None:
        payload["start_date"] = start_date
    if deadline is not None:
        payload["deadline"] = deadline
    if bill_service_id is not None:
        payload["bill_service_id"] = bill_service_id
    if id is not None:
        endpoint = id_endpoint_map.get(Service.subprojects).format(id=id)
        resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        endpoint = noid_endpoint_map.get(Service.subprojects)
        resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def create_or_update_team(
    name: Optional[str] = None,
    leader: Optional[int] = None,
    id: Optional[int] = None
) -> dict:
    """
    Create or update a team.
    If id is provided, updates the team, else creates a new team.
    Fields:
        name: Team name (required for create, max 100 chars)
        leader: User ID of the team leader
        id: Team ID for update
    """
    payload = {}
    if name is not None:
        payload["name"] = name
    if leader is not None:
        payload["leader"] = leader
    if id is not None:
        endpoint = id_endpoint_map.get(Service.teams).format(id=id)
        resp = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        endpoint = noid_endpoint_map.get(Service.teams)
        resp = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return resp.json()


@mcp.tool()
def create_or_update_usersnonbusinessgroup(
    users_id: int,
    nonbusiness_groups_id: int,
    date_since: str,
    date_until: Optional[Union[str, None]] = None,
    id: Optional[int] = None
) -> dict:
    """
    Create or update a usersnonbusinessgroup assignment.
    If `id` is provided, updates the assignment; otherwise, creates a new one.
    date_since: Start date (YYYY-MM-DD). Example: "2025-01-31"
    date_until: End date (YYYY-MM-DD or null). Example: "2025-02-28"
    """
    payload = {
        "users_id": users_id,
        "nonbusiness_groups_id": nonbusiness_groups_id,
        "date_since": date_since,
    }
    if date_until is not None:
        payload["date_until"] = date_until
    if id is not None:
        endpoint = id_endpoint_map.get(Service.usersnonbusinessgroups).format(id=id)
        response = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        endpoint = noid_endpoint_map.get(Service.usersnonbusinessgroups)
        response = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return response.json()


@mcp.tool()
def create_or_update_absence(
    date_since: str,
    type: str,
    users_id: Optional[int] = None,
    date_until: Optional[str] = None,
    half_day: Optional[bool] = None,
    count_hours: Optional[float] = None,
    allow_override: Optional[list[int]] = None,
    status: Optional[AbsenceStatus] = None,
    sick_note: Optional[bool] = None,
    note: Optional[str] = None,
    public_note: Optional[str] = None,
    id: Optional[int] = None
) -> dict:
    """
    Create or update an absence entry.
    If `id` is provided, updates the absence; otherwise, creates a new one.
    Fields:
        date_since: Start date (YYYY-MM-DD). Example: "2023-02-28"
        type: Absence type. Example: "vacation"
        users_id: User ID. Example: 42
        date_until: End date (YYYY-MM-DD or null). Example: "2023-03-01"
        half_day: Is half day absence
        count_hours: Number of hours (float). Example: 8.0
        allow_override: List of absence IDs to override in case of conflicts
        status: Absence status. Possible values:
    - `0`: Enquired
    - `1`: Approved
    - `2`: Declined
    - `3`: ApprovalCancelled
    - `4`: Cancelled
        sick_note: Is sick note. Example: False
        note: Internal note. Example: "Doctor's appointment"
        public_note: Public note. Example: "Vacation"
        id: Absence ID (for update only)
    """
    payload = {
        "date_since": date_since,
        "type": type,
    }
    if users_id is not None:
        payload["users_id"] = users_id
    if date_until is not None:
        payload["date_until"] = date_until
    if half_day is not None:
        payload["half_day"] = half_day
    if count_hours is not None:
        payload["count_hours"] = count_hours
    if allow_override is not None:
        payload["allow_override"] = allow_override
    if status is not None:
        payload["status"] = status.value
    if sick_note is not None:
        payload["sick_note"] = sick_note
    if note is not None:
        payload["note"] = note
    if public_note is not None:
        payload["public_note"] = public_note
    if id is not None:
        endpoint = id_endpoint_map.get(Service.absences).format(id=id)
        response = requests.put(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    else:
        # Create new absence
        endpoint = noid_endpoint_map.get(Service.absences)
        response = requests.post(BASE_URL + endpoint, headers=AUTH_HEADERS, json=payload)
    return response.json()


