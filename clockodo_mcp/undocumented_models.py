
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

from pydantic import Field

class UserGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = Field(None, example={"active": True, "fulltext": "search", "teams_id": [1, 2]})
    scope: Optional[str] = Field(None, example="all")
    sort: Optional[List[Any]] = Field(None, example=[{"id": 1, "name": "User"}])
    page: Optional[int] = Field(None, example=1)
    items_per_page: Optional[int] = Field(None, example=100)

class EntryGetParams(BaseModel):
    time_since: str = Field(..., example="2023-02-28T12:00:00Z")
    time_until: str = Field(..., example="2023-02-28T12:00:00Z")
    calc_also_revenues_for_projects_with_hard_budget: Optional[bool] = Field(None, example=True)
    enhanced_list: Optional[bool] = Field(None, example=False)
    filter: Optional[Dict[str, Any]] = Field(None, example={"users_id": 123})
    page: Optional[int] = Field(None, example=1)
    items_per_page: Optional[int] = Field(None, example=100)

# Customer GET
class CustomerGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = Field(None, example={"active": True, "fulltext": "search"})
    sort: Optional[List[Any]] = Field(None, example=[{"id": 1, "name": "Customer", "active": True}])
    scope: Optional[str] = Field(None, example="all")
    page: Optional[int] = Field(None, example=1)
    items_per_page: Optional[int] = Field(None, example=100)

# Project GET
class ProjectGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = Field(None, example={"active": True})
    sort: Optional[List[Any]] = Field(None, example=[{"id": 1, "name": "Project"}])
    scope: Optional[str] = Field(None, example="all")
    page: Optional[int] = Field(None, example=1)
    items_per_page: Optional[int] = Field(None, example=100)

# Service GET
class ServiceGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = Field(None, example={"active": True})
    sort: Optional[List[Any]] = Field(None, example=[{"id": 1, "name": "Service"}])
    scope: Optional[str] = Field(None, example="all")
    page: Optional[int] = Field(None, example=1)
    items_per_page: Optional[int] = Field(None, example=100)

# Team GET
class TeamGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = Field(None, example={"active": True})
    scope: Optional[str] = Field(None, example="all")
    sort: Optional[List[Any]] = Field(None, example=[{"id": 1, "name": "Team"}])
    page: Optional[int] = Field(None, example=1)
    items_per_page: Optional[int] = Field(None, example=100)

# Absence GET
class AbsenceGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = Field(None, example={"type": "holiday"})
    sort: Optional[List[Any]] = Field(None, example=[{"id": 1, "name": "Absence"}])
    scope: Optional[str] = Field(None, example="all")
    page: Optional[int] = Field(None, example=1)
    items_per_page: Optional[int] = Field(None, example=100)

# Subproject GET
class SubprojectGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = Field(None, example={"active": True})
    sort: Optional[List[Any]] = Field(None, example=[{"id": 1, "name": "Subproject"}])
    page: Optional[int] = Field(None, example=1)
    items_per_page: Optional[int] = Field(None, example=100)

# Holiday Quota GET
class HolidayQuotaGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = Field(None, example={"active": True})
    users_id: Optional[int] = Field(None, example=123)
    year: Optional[int] = Field(None, example=2023)

# Work Time GET
class WorkTimeGetParams(BaseModel):
    date_since: str = Field(..., example="2023-02-01")
    date_until: str = Field(..., example="2023-02-28")
    users_id: int = Field(..., example=123)

# Nonbusiness Day GET
class NonbusinessDayGetParams(BaseModel):
    year: Optional[int] = Field(None, example=2023)
    nonbusiness_group_id: Optional[List[int]] = Field(None, example=[1,2])

# Overtime Carry GET
class OvertimeCarryGetParams(BaseModel):
    year: Optional[int] = Field(None, example=2023)
    users_id: Optional[int] = Field(None, example=123)

# Overtime Reduction GET
class OvertimeReductionGetParams(BaseModel):
    users_id: Optional[List[int]] = Field(None, example=[123, 456])

# Lump Sum Service GET
class LumpSumServiceGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = Field(None, example={"active": True})
    sort: Optional[List[Any]] = Field(None, example=[{"id": 1, "name": "LumpSumService"}])
    scope: Optional[str] = Field(None, example="all")
    page: Optional[int] = Field(None, example=1)
    items_per_page: Optional[int] = Field(None, example=100)

# Entry Group GET
class EntryGroupGetParams(BaseModel):
    time_since: str = Field(..., example="2023-02-01T00:00:00Z")
    time_until: str = Field(..., example="2023-02-28T23:59:59Z")
    grouping: List[Any] = Field(..., example=["project", "service"])
    round_to_minutes: Optional[int] = Field(None, example=15)
    prepend_customer_to_project_name: Optional[bool] = Field(None, example=True)
    calc_also_revenues_for_projects_with_hard_budget: Optional[bool] = Field(None, example=True)
    filter: Optional[Dict[str, Any]] = Field(None, example={"users_id": 123})

# Target Hour GET
class TargetHourGetParams(BaseModel):
    users_id: Optional[List[int]] = Field(None, example=[123, 456])

# User Report GET
class UserReportGetParams(BaseModel):
    year: int = Field(..., example=2023)
    type: Optional[int] = Field(None, example=1)

# Access Group GET
class AccessGroupGetParams(BaseModel):
    pass  # No parameters

# Register GET (not supported)
class RegisterGetParams(BaseModel):
    pass  # Not supported



# models for delete calls
# Generic model for delete by id (most resources)
class DeleteByIdParams(BaseModel):
    id: int = Field(..., example=123)

# Model for delete calls supporting dry_run and force (customer, project, subproject, lump_sum_service, project)
class DeleteByIdDryRunForceParams(BaseModel):
    id: int = Field(..., example=123)
    dry_run: Optional[bool] = Field(None, example=True)
    force: Optional[bool] = Field(None, example=True)

# Model for entry_group delete (uses time_since and time_until)
class DeleteEntryGroupParams(BaseModel):
    time_since: str = Field(..., example="2023-02-01T00:00:00Z")
    time_until: str = Field(..., example="2023-02-28T23:59:59Z")
