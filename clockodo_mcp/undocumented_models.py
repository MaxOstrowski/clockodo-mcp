from pydantic import BaseModel
from typing import Optional, List, Dict, Any

# Entry GET
class EntryGetParams(BaseModel):
    time_since: str
    time_until: str
    calc_also_revenues_for_projects_with_hard_budget: Optional[bool] = None
    enhanced_list: Optional[bool] = None
    filter: Optional[Dict[str, Any]] = None
    page: Optional[int] = None
    items_per_page: Optional[int] = None

# Customer GET
class CustomerGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = None
    sort: Optional[List[Any]] = None
    scope: Optional[str] = None
    page: Optional[int] = None
    items_per_page: Optional[int] = None

# Project GET
class ProjectGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = None
    sort: Optional[List[Any]] = None
    scope: Optional[str] = None
    page: Optional[int] = None
    items_per_page: Optional[int] = None

# Service GET
class ServiceGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = None
    sort: Optional[List[Any]] = None
    scope: Optional[str] = None
    page: Optional[int] = None
    items_per_page: Optional[int] = None

# Team GET
class TeamGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = None
    scope: Optional[str] = None
    sort: Optional[List[Any]] = None
    page: Optional[int] = None
    items_per_page: Optional[int] = None

# Absence GET
class AbsenceGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = None
    sort: Optional[List[Any]] = None
    scope: Optional[str] = None
    page: Optional[int] = None
    items_per_page: Optional[int] = None

# Subproject GET
class SubprojectGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = None
    sort: Optional[List[Any]] = None
    page: Optional[int] = None
    items_per_page: Optional[int] = None

# Holiday Quota GET
class HolidayQuotaGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = None
    users_id: Optional[int] = None
    year: Optional[int] = None

# Work Time GET
class WorkTimeGetParams(BaseModel):
    date_since: str
    date_until: str
    users_id: int

# Nonbusiness Day GET
class NonbusinessDayGetParams(BaseModel):
    year: Optional[int] = None
    nonbusiness_group_id: Optional[List[int]] = None

# Overtime Carry GET
class OvertimeCarryGetParams(BaseModel):
    year: Optional[int] = None
    users_id: Optional[int] = None

# Overtime Reduction GET
class OvertimeReductionGetParams(BaseModel):
    users_id: Optional[List[int]] = None

# Lump Sum Service GET
class LumpSumServiceGetParams(BaseModel):
    filter: Optional[Dict[str, Any]] = None
    sort: Optional[List[Any]] = None
    scope: Optional[str] = None
    page: Optional[int] = None
    items_per_page: Optional[int] = None

# Entry Group GET
class EntryGroupGetParams(BaseModel):
    time_since: str
    time_until: str
    grouping: List[Any]
    round_to_minutes: Optional[int] = None
    prepend_customer_to_project_name: Optional[bool] = None
    calc_also_revenues_for_projects_with_hard_budget: Optional[bool] = None
    filter: Optional[Dict[str, Any]] = None

# Target Hour GET
class TargetHourGetParams(BaseModel):
    users_id: Optional[List[int]] = None

# User Report GET
class UserReportGetParams(BaseModel):
    year: int
    type: Optional[int] = None

# Access Group GET
class AccessGroupGetParams(BaseModel):
    pass

# Register GET (not supported)
class RegisterGetParams(BaseModel):
    pass



# models for delete calls
# Generic model for delete by id (most resources)
class DeleteByIdParams(BaseModel):
    id: int

# Model for delete calls supporting dry_run and force (customer, project, subproject, lump_sum_service, project)
class DeleteByIdDryRunForceParams(BaseModel):
    id: int
    dry_run: Optional[bool] = None
    force: Optional[bool] = None

# Model for entry_group delete (uses time_since and time_until)
class DeleteEntryGroupParams(BaseModel):
    time_since: str
    time_until: str
