from pydantic import BaseModel, Field
from clockodo_mcp.clockodo_mcp import AUTH_HEADERS, BASE_URL, mcp
from clockodo_mcp.models import AccessType, AccessValue, ChangeRequestIntervalType, TargetHourType
from clockodo_mcp.utils import Service, flatten_dict, noid_endpoint_map, id_endpoint_map
import requests
from typing import Optional

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
		holiday_fixed_credit (int): Fixed holiday credit. Enum: [0, 1]. Example: 1
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


