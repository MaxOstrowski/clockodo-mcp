from typing import Optional, List
from enum import Enum



from pydantic import BaseModel, Field

class Billable(Enum):
    NotBillable = 0
    Billable = 1
    Billed = 2
    BillableOrBilled = 12


class BillableDistinct(Enum):
    NotBillable = 0
    Billable = 1
    Billed = 2

class BudgetOption(Enum):
    Strict = "rep_filter_budget_strict"
    StrictCompleted = "rep_filter_budget_strict_completed"
    StrictIncomplete = "rep_filter_budget_strict_incomplete"
    Soft = "rep_filter_budget_soft"
    SoftCompleted = "rep_filter_budget_soft_completed"
    SoftIncomplete = "rep_filter_budget_soft_incomplete"
    Without = "rep_filter_budget_without"
    WithoutStrict = "rep_filter_budget_without_strict"

class BudgetSource(Enum):
    NoBudget = 0
    EnterBudget = 1
    GetBudgetThroughSubprojects = 2
    Interval = 3

class ChangeRequestIntervalType(Enum):
    Added = 1
    Removed = 2

class ChangeRequestStatus(Enum):
    Requested = 1
    Declined = 2

class CustomerColor(Enum):
    BloodOrange = 1
    Sunflower = 2
    LightGreen = 3
    Caribbean = 4
    Sky = 5
    BrandBlue = 6
    BluePurple = 7
    Magenta = 8
    ChewingGum = 9

class DayAbsenceType(Enum):
    RegularHoliday = 1
    SpecialLeave = 2
    SickSelf = 4
    SickChild = 5
    School = 6
    MaternityProtection = 7
    HomeOffice = 8
    OutOfOffice = 9
    SpecialLeaveUnpaid = 10
    SickSelfUnpaid = 11
    SickChildUnpaid = 12
    Quarantine = 13
    MilitaryService = 14
    SickSelfWithCertificate = 15

class EditLockDay(Enum):
    LockDays1 = 1
    LockDays2 = 2
    LockDays3 = 3
    LockDays5 = 5
    LockDays8 = 8
    LockDays15 = 15
    LockDays31 = 31
    LockDays46 = 46
    LockDays91 = 91

class EntryTextMode(Enum):
    Add = "add"
    Edit = "edit"
    Reports = "reports"

class Grouping(Enum):
    Billable = "billable"
    CustomersId = "customers_id"
    Day = "day"
    Month = "month"
    IsLumpSum = "is_lumpsum"
    LumpSumServicesId = "lumpsum_services_id"
    ProjectsId = "projects_id"
    ServicesId = "services_id"
    SubprojectsId = "subprojects_id"
    TextsId = "texts_id"
    UsersId = "users_id"
    Week = "week"
    Year = "year"

class Language(Enum):
    English = "en"
    French = "fr"
    German = "de"

class MenuIcon(Enum):
    Briefcase = "briefcase"
    ChartBar = "chart-bar"
    Code = "code"
    Cog = "cog"
    Holiday = "holiday"
    Home = "home"
    FolderOpen = "folder-open"
    Planner = "planner"
    PlusCircle = "plus-circle"
    Share = "share"
    Star = "star"
    Stopwatch = "stopwatch"
    TeamHoliday = "team-holiday"
    Template = "template"
    Timetable = "timetable"
    UserGroup = "user-group"
    UserHoliday = "user-holiday"
    Users = "users"

class NonbusinessDayType(Enum):
    Special = "SPECIAL"
    DistinctOnce = "DISTINCT_ONCE"
    DistinctRecurring = "DISTINCT_RECURRING"

class Role(Enum):
    Worker = "worker"
    Owner = "owner"

class ServiceScope(Enum):
    ManageAccess = "manageAccess"

class TargetHourType(Enum):
    Weekly = "weekly"
    Monthly = "monthly"

class Thresholds(Enum):
    Percent50 = 50
    Percent60 = 60
    Percent70 = 70
    Percent80 = 80
    Percent90 = 90
    Percent100 = 100
    Percent110 = 110
    Percent120 = 120
    Percent130 = 130
    Percent140 = 140
    Percent150 = 150
    Percent200 = 200
    Percent250 = 250
    Percent300 = 300

class ApiProjectsReportsV3_SortForIndex(Enum):
    CustomersNameAsc = "customers_name"
    CustomersNameDesc = "-customers_name"
    ProjectsNameAsc = "projects_name"
    ProjectsNameDesc = "-projects_name"

class ApiProjectsReportsV4_SortForIndex(Enum):
    CustomersNameAsc = "customers_name"
    CustomersNameDesc = "-customers_name"
    ProjectsNameAsc = "projects_name"
    ProjectsNameDesc = "-projects_name"

class ApiUsersV3_SortForIndex(Enum):
    ActiveAsc = "active"
    ActiveDesc = "-active"
    IdAsc = "id"
    IdDesc = "-id"
    NameAsc = "name"
    NameDesc = "-name"
    NumberAsc = "number"
    NumberDesc = "-number"
    RoleAsc = "role"
    RoleDesc = "-role"
    TeamsNameAsc = "teams_name"
    TeamsNameDesc = "-teams_name"

class SortIdName(Enum):
    IdAsc = "id"
    IdDesc = "-id"
    NameAsc = "name"
    NameDesc = "-name"

class SortIdNameActive(Enum):
    ActiveAsc = "active"
    ActiveDesc = "-active"
    IdAsc = "id"
    IdDesc = "-id"
    NameAsc = "name"
    NameDesc = "-name"

class UserReportType(Enum):
    Year = 0
    Month = 1
    Week = 2
    Day = 3
    DayWithWorkTime = 4

class WageType(Enum):
    All = 0
    Salary = 1
    HourlyWage = 2

class UserScope(Enum):
    ManageAbsences = "manageAbsences"
    ViewAbsences = "viewAbsences"
    ViewUserReports = "viewUserReports"
    ViewUserReportsDetailed = "viewUserReportsDetailed"
    ViewPresences = "viewPresences"

# --- User Report Models ---
class UserReportAbsenceSummaryV1(BaseModel):
    regular_holidays: float
    sick_self: float
    sick_child: float
    special_leaves: float
    school: float
    maternity_protection: float
    home_office: float
    out_of_office: float
    quarantine: float
    military_service: float

class UserReportBreakItemV1(BaseModel):
    since: str
    until: str
    length: float

class UserReportSurchargeSummaryV1(BaseModel):
    saturday: float
    sunday: float
    nonbusiness: float
    nonbusiness_special: float
    night: float
    night_increased: float

class UserReportDayDetailV1(BaseModel):
    date: str
    weekday: int
    nonbusiness: bool
    count_absence: UserReportAbsenceSummaryV1
    count_reduction_used: Optional[float]
    target: Optional[float]
    target_raw: Optional[float]
    surcharges: UserReportSurchargeSummaryV1
    hours: Optional[float]
    hours_without_compensation: Optional[float]
    diff: float
    breaks: List[UserReportBreakItemV1]
    work_start: Optional[str]
    work_end: Optional[str]

class UserReportWeekDetailV1(BaseModel):
    nr: int
    sum_target: Optional[float]
    sum_hours: float
    sum_reduction_used: float
    diff: float
    surcharges: UserReportSurchargeSummaryV1
    day_details: Optional[List[UserReportDayDetailV1]]

class UserReportMonthDetailV1(BaseModel):
    nr: int
    sum_target: Optional[float]
    sum_hours: float
    sum_hours_without_compensation: float
    sum_reduction_used: float
    sum_overtime_reduced: float
    diff: float
    surcharges: UserReportSurchargeSummaryV1
    week_details: Optional[List[UserReportWeekDetailV1]]

class UserReportV1(BaseModel):
    users_id: int
    users_name: str
    users_number: Optional[str]
    users_email: str
    sum_target: Optional[float]
    sum_hours: float
    sum_reduction_used: float
    sum_reduction_planned: float
    overtime_carryover: float
    overtime_reduced: float
    diff: float
    holidays_quota: float
    holidays_carry: float
    sum_absence: UserReportAbsenceSummaryV1
    surcharges: UserReportSurchargeSummaryV1
    workdays: float
    month_details: Optional[List[UserReportMonthDetailV1]]
    type: Optional[UserReportType] = None  # Added for OpenAPI compatibility

class RegisterPayload(BaseModel):
    companies_name: str = Field(..., max_length=100, description="Company name")
    name: str = Field(..., max_length=100, description="User's name")
    email: str = Field(..., description="User's email address")
    rfs: Optional[str] = Field(None, description="Name of the external application from which the registration is made")
    bs: Optional[str] = Field(None, description="Preselected billing application")
    gtc_agreed: Optional[str] = Field(None, description="Terms of Clockodo were accepted")

class BudgetTotalErrorDetails(BaseModel):
    max: float
    budget_is_hours: bool

class OnlyOwnerCanDeleteOwnerError(BaseModel):
    type: str
    message: Optional[str]
    path: Optional[str]
    details: Optional[None]

class OvertimeCarryV3(BaseModel):
    id: int
    users_id: int
    year: int
    hours: float
    note: Optional[str]

class OvertimeReductionV3(BaseModel):
    id: int
    users_id: int
    date: str
    hours: float
    note: Optional[str]
    added_at: str
    added_by_users_id: int

class ProjectReportsV3(BaseModel):
    customers_id: int
    customers_name: str
    customers_number: Optional[str]
    projects_id: int
    projects_name: str
    projects_number: Optional[str]
    budget_source: Optional[List[BudgetSource]] = None

class ProjectsReportProjectReportItemV4(BaseModel):
    customers_id: int
    customers_name: str
    customers_number: Optional[str]
    projects_id: int
    projects_name: str
    projects_number: Optional[str]
    budget_source: Optional[List[BudgetSource]] = None

class ProjectsReportRetainerSubprojectReportItemV4(BaseModel):
    customers_id: int
    customers_name: str
    customers_number: Optional[str]
    projects_id: int
    projects_name: str
    projects_number: Optional[str]
    subprojects_id: int
    subprojects_name: str
    subprojects_number: Optional[str]

class ProjectV4_Budget(BaseModel):
    monetary: bool
    hard: bool
    from_subprojects: bool
    interval: Optional[int]
    amount: Optional[float]
    notification_thresholds: Optional[List[Thresholds]]

class ProjectV4(BaseModel):
    id: int
    customers_id: int
    name: str
    number: Optional[str]
    active: bool
    billable_default: bool
    note: Optional[str]
    billed_money: Optional[float]
    billed_completely: Optional[bool]
    completed: bool
    completed_at: Optional[str]
    revenue_factor: Optional[float]
    test_data: bool
    count_subprojects: int
    deadline: Optional[str]
    start_date: Optional[str]
    budget: Optional[ProjectV4_Budget]
    bill_service_id: Optional[str]

ProjectV4.update_forward_refs()

class RateV3(BaseModel):
    id: int
    customer_ids: List[int]
    project_ids: List[int]
    service_ids: List[int]
    user_ids: List[int]
    hourly_rate: float
    test_data: bool
    children: List[RateV3]

RateV3.update_forward_refs()

class RegisterV1(BaseModel):
    success: bool
    user: Optional[dict]  # Should be SettingV1, placeholder
    apikey: str
    first_login_key: Optional[str]

class Resource(BaseModel):
    resources: List[str]

class ResourcesInactive(BaseModel):
    inactive_ids: List[int]

class ResourcesNotFound(BaseModel):
    not_found_ids: List[int]

class TeamV3(BaseModel):
    id: int
    name: str
    leader: Optional[int]

class BlockingAccessDependencies(BaseModel):
    access_name: str
    elevated_access_dependencies: Optional[List[str]]

class EntryV2Time(BaseModel):
    id: int
    customers_id: int
    projects_id: Optional[int]
    subprojects_id: Optional[int]
    users_id: int
    billable: int
    texts_id: Optional[int]
    text: Optional[str]
    time_since: str
    time_until: Optional[str]
    time_insert: str
    time_last_change: str
    test_data: bool
    customers_name: str
    projects_name: Optional[str]
    subprojects_name: Optional[str]
    users_name: str
    revenue: Optional[float]
    type: int
    services_id: Optional[int]
    duration: Optional[int]
    time_last_change_work_time: str
    time_clocked_since: Optional[str]
    clocked: bool
    clocked_offline: bool
    hourly_rate: Optional[float]
    services_name: str

class UserV3(BaseModel):
    id: int
    name: str
    weekstart_monday: bool
    weekend_friday: bool
    active: bool
    timeformat_12h: bool
    language: str
    timezone: str
    teams_id: Optional[int]
    initials: str
    nonbusiness_groups_id: Optional[int]
    number: Optional[str]
    work_time_regulations_id: Optional[int]
    default_work_time_regulation: Optional[bool]
    boss: Optional[int]
    absence_managers_id: Optional[List[int]]
    email: str
    role: Role
    can_generally_see_absences: Optional[bool]
    can_generally_manage_absences: Optional[bool]
    can_add_customers: Optional[bool]
    default_holidays_count: Optional[bool]
    default_target_hours: Optional[bool]
    future_coworker: Optional[bool]
    start_date: Optional[str]
    wage_type: Optional[str]

class TargetHourV1(BaseModel):
    id: int
    users_id: int
    surcharge_models_id: Optional[int]
    type: TargetHourType
    date_since: str
    date_until: Optional[str]
    test_data: bool
    monday: float
    tuesday: float
    wednesday: float
    thursday: float
    friday: float
    saturday: float
    sunday: float
    absence_fixed_credit: bool
    compensation_daily: float
    compensation_monthly: float
    workday_monday: bool
    workday_tuesday: bool
    workday_wednesday: bool
    workday_thursday: bool
    workday_friday: bool
    workday_saturday: bool
    workday_sunday: bool
    monthly_target: float

# Fix forward references for Pydantic models
ProjectV4.update_forward_refs()
RateV3.update_forward_refs()

class TargetHourPayload(BaseModel):
    users_id: int = Field(..., description="User ID")
    type: TargetHourType = Field(..., description="Target hour type")
    date_since: str = Field(..., description="Start date (YYYY-MM-DD)")
    date_until: Optional[str] = Field(None, description="End date (YYYY-MM-DD)")
    monday: Optional[float] = Field(None, description="Monday target hours")
    tuesday: Optional[float] = Field(None, description="Tuesday target hours")
    wednesday: Optional[float] = Field(None, description="Wednesday target hours")
    thursday: Optional[float] = Field(None, description="Thursday target hours")
    friday: Optional[float] = Field(None, description="Friday target hours")
    saturday: Optional[float] = Field(None, description="Saturday target hours")
    sunday: Optional[float] = Field(None, description="Sunday target hours")
    monthly_target: Optional[float] = Field(None, description="Monthly target hours")
    workday_monday: Optional[bool] = Field(None, description="Is Monday a workday?")
    workday_tuesday: Optional[bool] = Field(None, description="Is Tuesday a workday?")
    workday_wednesday: Optional[bool] = Field(None, description="Is Wednesday a workday?")
    workday_thursday: Optional[bool] = Field(None, description="Is Thursday a workday?")
    workday_friday: Optional[bool] = Field(None, description="Is Friday a workday?")
    workday_saturday: Optional[bool] = Field(None, description="Is Saturday a workday?")
    workday_sunday: Optional[bool] = Field(None, description="Is Sunday a workday?")
    compensation_daily: Optional[float] = Field(None, description="Automatic time compensation per day in minutes")
    compensation_monthly: float = Field(..., description="Compensation for monthly target hours in minutes")
    holiday_fixed_credit: Optional[int] = Field(None, description="Holiday fixed credit (0 or 1)")
    surcharge_models_id: Optional[int] = Field(None, description="Surcharge model ID")

class AccessGroupPayload(BaseModel):
    name: str = Field(..., max_length=100, description="Access group name")
    users_ids: Optional[List[int]] = Field(None, description="IDs of the access group members")

class EntryPayload(BaseModel):
    time_since: Optional[str] = Field(None, description="Start time (ISO 8601)")
    time_until: Optional[str] = Field(None, description="End time (ISO 8601)")
    customers_id: int = Field(..., description="Customer ID")
    billable: Billable = Field(..., description="Billable status")
    projects_id: Optional[int] = Field(None, description="Project ID")
    subprojects_id: Optional[int] = Field(None, description="Subproject ID")
    services_id: Optional[int] = Field(None, description="Service ID")
    lumpsum_services_id: Optional[int] = Field(None, description="Lump sum service ID")
    users_id: Optional[int] = Field(None, description="User ID")
    clocked_offline: Optional[bool] = Field(None, description="Clocked offline")
    duration: Optional[int] = Field(None, description="Duration in seconds")
    lumpsum: Optional[float] = Field(None, description="Lump sum amount")
    hourly_rate: Optional[float] = Field(None, description="Hourly rate")
    lumpsum_services_amount: Optional[float] = Field(None, description="Lump sum services amount")
    text: Optional[str] = Field(None, description="Entry text")
    time_clocked_since: Optional[str] = Field(None, description="Time clocked since (ISO 8601)")
    budget_type: Optional[BudgetOption] = Field(None, description="Budget type")

class EntryGroupPayload(BaseModel):
    time_since: str = Field(..., description="Start time (ISO 8601)")
    time_until: str = Field(..., description="End time (ISO 8601)")
    users_id: Optional[int] = Field(None, description="User ID")
    customers_id: Optional[int] = Field(None, description="Customer ID")
    projects_id: Optional[int] = Field(None, description="Project ID")
    subprojects_id: Optional[int] = Field(None, description="Subproject ID")
    services_id: Optional[int] = Field(None, description="Service ID")
    lumpsum_services_id: Optional[int] = Field(None, description="Lump sum service ID")
    billable: Optional[BillableDistinct] = Field(None, description="Billable status (distinct)")
    text: Optional[str] = Field(None, description="Entry group text")
    hourly_rate: Optional[float] = Field(None, description="Hourly rate")
    confirm_key: Optional[str] = Field(None, description="Confirmation key for edit action")
    filter: Optional[dict] = Field(None, description="Filter object for entry group")
    budget_type: Optional[BudgetOption] = Field(None, description="Budget type")
    grouping: Optional[List[Grouping]] = Field(None, description="Grouping options")

class HolidayQuotaPayload(BaseModel):
    users_id: int = Field(..., description="User ID")
    year_since: int = Field(..., description="Year from which the holiday quota applies")
    year_until: Optional[int] = Field(None, description="Year until the holiday quota applies")
    count: float = Field(..., description="Amount of holidays")
    note: Optional[str] = Field(None, description="Note (max 1000 chars)")

class NonbusinessDayPayload(BaseModel):
    nonbusiness_group_id: int = Field(..., description="Default: Company default nonbusiness group")
    type: NonbusinessDayType = Field(..., description="Type of nonbusiness day")
    name: str = Field(..., max_length=100, description="Name of the nonbusiness day")
    half_day: Optional[bool] = Field(None, description="Is it a half day?")
    surcharge_special: Optional[bool] = Field(None, description="Surcharge special")
    special_id: Optional[int] = Field(None, description="Special ID")
    day: Optional[int] = Field(None, description="Day of month")
    month: Optional[int] = Field(None, description="Month")
    year: Optional[int] = Field(None, description="Year")

class NonbusinessGroupPayload(BaseModel):
    name: str = Field(..., max_length=100, description="Nonbusiness group name")
    preset: Optional[str] = Field(None, description="Preset (enum: [''])")

class WorkTimesChangeRequestPayload(BaseModel):
    date: str = Field(..., description="Date (YYYY-MM-DD)")
    users_id: int = Field(..., description="User ID")
    changes: Optional[List[ChangeRequestIntervalType]] = Field(None, description="List of changes (intervals)")
    status: Optional[ChangeRequestStatus] = Field(None, description="Change request status")

class CustomerPayload(BaseModel):
    name: str = Field(..., max_length=100, description="Customer name")
    number: Optional[str] = Field(None, max_length=50, description="Freely selectable number for the customer")
    active: Optional[bool] = Field(None, description="Is the customer active?")
    billable_default: Optional[bool] = Field(None, description="Default billable status")
    note: Optional[str] = Field(None, max_length=1000, description="Note (owners/workers with elevated access only)")
    color: Optional[CustomerColor] = Field(None, description="Color code (1-9, see API docs)")
    bill_service_id: Optional[str] = Field(None, max_length=50, description="Billing application customer ID")

class HolidaysCarryPayload(BaseModel):
    year: int = Field(..., description="Year for which the holiday carryover applies")
    users_id: Optional[int] = Field(None, description="User ID")
    count: float = Field(..., description="Only full and half values allowed")
    note: Optional[str] = Field(None, max_length=1000, description="Note")

class OvertimeCarryPayload(BaseModel):
    year: int = Field(..., description="Year for which the overtime carry applies")
    users_id: Optional[int] = Field(None, description="User ID")
    hours: float = Field(..., description="Overtime hours (full/half values allowed)")
    note: Optional[str] = Field(None, max_length=1000, description="Note")

class OvertimeReductionPayload(BaseModel):
    users_id: int = Field(..., description="User ID")
    date: str = Field(..., description="Date (YYYY-MM-DD)")
    hours: float = Field(..., description="Reduction hours")
    note: Optional[str] = Field(None, max_length=1000, description="Note")

class SubprojectPayload(BaseModel):
    projects_id: Optional[int] = Field(None, description="Project ID")
    name: Optional[str] = Field(None, max_length=100, description="Subproject name")
    billable_default: Optional[bool] = Field(None, description="Default billable status")
    budget: Optional[dict] = Field(None, description="Budget object")
    number: Optional[str] = Field(None, max_length=50, description="Subproject number")
    note: Optional[str] = Field(None, max_length=1000, description="Note")
    start_date: Optional[str] = Field(None, description="Start date (YYYY-MM-DD)")
    deadline: Optional[str] = Field(None, description="Deadline (YYYY-MM-DD)")
    bill_service_id: Optional[str] = Field(None, max_length=50, description="Billing application subproject ID")

class TeamPayload(BaseModel):
    name: str = Field(..., max_length=100, description="Team name")
    leader: Optional[int] = Field(None, description="User ID of the team leader")

class UserPayload(BaseModel):
    email: str = Field(..., max_length=90, description="User email")
    name: str = Field(..., max_length=100, description="User name")
    role: Role = Field(..., description="User role")
    active: Optional[bool] = Field(None, description="Is the user active?")
    boss: Optional[int] = Field(None, description="Boss user ID")
    number: Optional[str] = Field(None, max_length=50, description="User number")
    language: Optional[Language] = Field(None, description="Language")
    teams_id: Optional[int] = Field(None, description="Team ID")
    timeformat_12h: Optional[bool] = Field(None, description="Use 12h time format?")
    timezone: Optional[str] = Field(None, description="Timezone")
    wage_type: Optional[WageType] = Field(None, description="Wage type")
    weekstart_monday: Optional[bool] = Field(None, description="Start week on Monday?")
    weekend_friday: Optional[bool] = Field(None, description="End week on Friday?")
    show_favorites: Optional[bool] = Field(None, description="Show favorites")
    mail_to_user: Optional[bool] = Field(None, description="Send mail to user?")
    start_date: Optional[str] = Field(None, description="Start date (YYYY-MM-DD)")
    budget_notifications: Optional[bool] = Field(None, description="Budget notifications")
    edit_lock: Optional[str] = Field(None, description="Edit lock date (YYYY-MM-DD)")
    edit_lock_dyn: Optional[EditLockDay] = Field(None, description="Dynamic edit lock")
    edit_lock_sync: Optional[bool] = Field(None, description="Edit lock sync")
    work_time_edit_lock_days: Optional[int] = Field(None, description="Work time edit lock days")
    default_holidays_count: Optional[bool] = Field(None, description="Use company default holiday count")
    default_target_hours: Optional[bool] = Field(None, description="Use company default target hours")
    work_time_regulations_id: Optional[int] = Field(None, description="Work time regulations ID")
    default_work_time_regulation: Optional[bool] = Field(None, description="Use company default work time regulation")
    absence_managers_id: Optional[List[int]] = Field(None, description="Absence managers IDs")
    access_groups_ids: Optional[List[int]] = Field(None, description="Access groups IDs")
    bill_service_id: Optional[str] = Field(None, max_length=50, description="Billing application user ID")

class UsersNonbusinessGroupPayload(BaseModel):
    users_id: int = Field(..., description="User ID")
    nonbusiness_groups_id: int = Field(..., description="Nonbusiness group ID")
    date_since: str = Field(..., description="Start date (YYYY-MM-DD)")
    date_until: Optional[str] = Field(None, description="End date (YYYY-MM-DD)")

class AbsencePayload(BaseModel):
    date_since: str = Field(..., description="Start date (YYYY-MM-DD)")
    date_until: Optional[str] = Field(None, description="End date (YYYY-MM-DD)")
    type: DayAbsenceType = Field(..., description="Absence type")
    half_day: Optional[bool] = Field(None, description="Is it a half day?")
    count_hours: Optional[float] = Field(None, description="Count hours")
    users_id: Optional[int] = Field(None, description="User ID")
    allow_override: Optional[List[int]] = Field(None, description="IDs of absences that may be shortened or deleted to avoid conflicts")
    status: Optional[str] = Field(None, description="Absence status")
    sick_note: Optional[bool] = Field(None, description="Sick note")
    note: Optional[str] = Field(None, max_length=512, description="Note")
    public_note: Optional[str] = Field(None, max_length=512, description="Public note")

class LumpSumServicePayload(BaseModel):
    name: str = Field(..., max_length=100, description="Lump sum service name")
    price: float = Field(..., description="Price per unit")
    unit: Optional[str] = Field(None, max_length=6, description="Unit")
    active: Optional[bool] = Field(None, description="Is the lump sum service active?")
    number: Optional[str] = Field(None, max_length=50, description="Lump sum service number")
    note: Optional[str] = Field(None, max_length=1000, description="Note (owners/workers with elevated access only)")

class ProjectPayload(BaseModel):
    name: str = Field(..., max_length=100, description="Project name")
    customers_id: int = Field(..., description="Customer ID")
    active: Optional[bool] = Field(None, description="Is the project active?")
    number: Optional[str] = Field(None, max_length=50, description="Project number")
    billable_default: Optional[bool] = Field(None, description="Default billable status")
    note: Optional[str] = Field(None, max_length=1000, description="Note")
    deadline: Optional[str] = Field(None, description="Deadline (YYYY-MM-DD)")
    start_date: Optional[str] = Field(None, description="Start date (YYYY-MM-DD)")
    budget: Optional[dict] = Field(None, description="Budget object")
    bill_service_id: Optional[str] = Field(None, max_length=50, description="Billing application project ID")

class ServicePayload(BaseModel):
    name: str = Field(..., max_length=100, description="Service name")
    active: Optional[bool] = Field(None, description="Is the service active?")
    number: Optional[str] = Field(None, max_length=50, description="Freely selectable number for the service")
    note: Optional[str] = Field(None, max_length=1000, description="Note (owners/workers with elevated access only)")
    bill_service_id: Optional[str] = Field(None, max_length=50, description="Billing application service ID")

class SortFilterPayload(BaseModel):
    sort_id_name: Optional[List[SortIdName]] = Field(None, description="Sort by id or name")
    sort_id_name_active: Optional[List[SortIdNameActive]] = Field(None, description="Sort by id, name, or active status")
    sort_users_v3: Optional[List[ApiUsersV3_SortForIndex]] = Field(None, description="Sort users by various fields")
    sort_projects_reports_v3: Optional[List[ApiProjectsReportsV3_SortForIndex]] = Field(None, description="Sort project reports by customer or project name")
    sort_projects_reports_v4: Optional[List[ApiProjectsReportsV4_SortForIndex]] = Field(None, description="Sort project reports V4 by customer or project name")

