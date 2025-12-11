from enum import Enum
from typing import Optional

from pydantic import BaseModel
import requests

from clockodo_mcp.models import BillableDistinct, BudgetOption
from clockodo_mcp.utils import DeleteEntrygroupV2Filter, Service, flatten_dict, id_endpoint_map, noid_endpoint_map
from clockodo_mcp.clockodo_mcp import AUTH_HEADERS, BASE_URL, mcp


class ServiceDeleteSingleId(Enum):
    """ list of services that support delete endpoint with and id"""
    targethours = Service.targethours.value
    accessgroups = Service.accessgroups.value
    entries = Service.entries.value
    holidaysquota = Service.holidaysquota.value
    nonbusinessdays = Service.nonbusinessdays.value
    nonbusinessgroups = Service.nonbusinessgroups.value
    worktimes = Service.worktimes.value
    customers = Service.customers.value
    holidayscarry = Service.holidayscarry.value
    overtimecarry = Service.overtimecarry.value
    overtimereductions = Service.overtimereductions.value
    projects = Service.projects.value
    subprojects = Service.subprojects.value
    teams = Service.teams.value
    users = Service.users.value
    usersnonbusinessgroups = Service.usersnonbusinessgroups.value
    absences = Service.absences.value
    lumpsumservices = Service.lumpsumservices.value
    services = Service.services.value
    worktimeschangerequest = Service.worktimeschangerequest.value


@mcp.tool()
def delete(service: ServiceDeleteSingleId, id: int, dry_run: Optional[bool], force: Optional[bool]) -> dict:
    """ Delete entity by ID. 

    Dryrun and force only available for customer, subproject, lumpsumservice, project, service.
    
    """
    # Map ServiceDeleteSingleId to Service enum for endpoint lookup
    try:
        service_enum = Service(service.value)
    except ValueError:
        raise ValueError(f"Invalid service value: {service.value}")
    endpoint_template = id_endpoint_map.get(service_enum)
    if not endpoint_template:
        raise ValueError(f"No endpoint mapping found for service: {service.value}")
    endpoint = endpoint_template.format(id=id)
    params = {}
    if dry_run is not None:
        params["dry_run"] = str(dry_run).lower()
    if force is not None:
        params["force"] = str(force).lower()

    resp = requests.request("DELETE", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()


@mcp.tool()
def delete_entrygroup(
        time_since: str,
        time_until: str,
        confirm_key: Optional[str] = None,
        filter: Optional[DeleteEntrygroupV2Filter] = None
    ) -> dict:
        """Delete entry groups by filter and time range

        time_since: Start of the time range (ISO 8601 string, required)
        time_until: End of the time range (ISO 8601 string, required)
        confirm_key: Optional confirmation key
        filter: Optional
        """
        endpoint_template = noid_endpoint_map.get(Service.entrygroups)
        params = {
            "time_since": time_since,
            "time_until": time_until,
        }
        if confirm_key is not None:
            params["confirm_key"] = confirm_key
        if filter is not None:
            filter_dict = filter.model_dump(exclude_none=True)
            params["filter"] = flatten_dict(filter_dict, parent_key="filter")
            
        resp = requests.request("DELETE", url=BASE_URL + endpoint_template, headers=AUTH_HEADERS, params=flatten_dict(params)
        )
        return resp.json()


@mcp.tool("restricted")
def delete_clock(id: int, away: Optional[int] = None, time_until: Optional[str] = None) -> dict:
    """Stop the clock by ID.

    id: Clock ID (required)
    away: Optional user ID to set as away
    time_until: Optional date-time string until which the away status should be set
    """
    endpoint_template = id_endpoint_map.get(Service.clock)
    if not endpoint_template:
        raise ValueError("No endpoint mapping found for Service.worktimes")
    endpoint = endpoint_template.format(id=id)
    params = {}
    if away is not None:
        params["away"] = away
    if time_until is not None:
        params["time_until"] = time_until
    resp = requests.request("DELETE", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=flatten_dict(params))
    return resp.json()