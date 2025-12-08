

from enum import Enum
from typing import Optional

import requests

from clockodo_mcp.utils import Service, id_endpoint_map
from clockodo_mcp.clockodo_mcp import AUTH_HEADERS, BASE_URL, mcp


class ServiceDeleteSingleId(Enum):
    """ list of services that support delete endpoint with and id"""
    targethours = Service.targethours.value
    accessgroups = Service.accessgroups.value
    entries = Service.entries.value
    holidaysquota = Service.holidaysquota.value
    nonbusinessdays = Service.nonbusinessdays.value
    nonbusinessgroups = Service.nonbusinessgroups.value
    holidayscarry = Service.holidayscarry.value
    overtimecarry = Service.overtimecarry.value
    overtimereductions = Service.overtimereductions.value
    teams = Service.teams.value
    users = Service.users.value
    usersnonbusinessgroups = Service.usersnonbusinessgroups.value
    absences = Service.absences.value
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

    resp = requests.request("DELETE", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=params)
    return resp.json()


@mcp.tool()
def delete_entrygroup(id: int,
                      away: Optional[int] = None,
                      time_until: Optional[str] = None,
                      users_id: Optional[int] = None,
                      start_new: Optional[bool] = None) -> dict:
    """ Delete entry group by ID.

    away: User ID to set as away user after deleting the entry group.
    time_until: Date-time string until which the away status should be set, example: '2023-02-28T12:00:00Z'.
    users_id: User ID for whom the entry group should be deleted.
    start_new: Whether to start a new clock entry after deleting the entry group. 
    """
    endpoint_template = id_endpoint_map.get(Service.entrygroups)
    if not endpoint_template:
        raise ValueError(f"No endpoint mapping found for service: {Service.entrygroups.value}")
    endpoint = endpoint_template.format(id=id)
    params = {}
    if away is not None:
        params["away"] = str(away).lower()
    if time_until is not None:
        params["time_until"] = time_until
    if users_id is not None:
        params["users_id"] = users_id
    if start_new is not None:
        params["start_new"] = str(start_new).lower()

    resp = requests.request("DELETE", url=BASE_URL + endpoint, headers=AUTH_HEADERS, params=params)
    return resp.json()