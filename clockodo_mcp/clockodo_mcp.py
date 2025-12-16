"""Clockodo MCP Server implementation."""

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os

load_dotenv()
AUTH_HEADERS = {
    "X-ClockodoApiUser": os.getenv("CLOCKODO_API_USER"),
    "X-ClockodoApiKey": os.getenv("CLOCKODO_API_KEY"),
    "X-Clockodo-External-Application": os.getenv("CLOCKODO_EXTERNAL_APP"),
}

BASE_URL = "https://my.clockodo.com/api"

class ToolRestrictor:
    def __init__(self):
        self.collected_tools = []
        self.mcp = FastMCP("""Clockodo MCP Server
This MCP server provides integration with the Clockodo time tracking API.
It allows querying, creating, and updating time entries (entries), users, projects(subprojects), and more.
Use this server to automate and analyze your time tracking data.
                           
 - targethours: Expected (planned) working hours for users.
 - userreports: Reports summarizing user activity and time tracking.
 - worktimes: Actual recorded work times for users.
 - accessgroups: Groups that define access permissions for users.
 - clock: Start or stop a running time entry (clock).
 - entries: Individual time entries (work logs).
 - entries_texts: Additional notes or texts attached to time entries.
 - entrygroups: Aggregated (grouped) time entries, e.g., by project or user.
 - holidaysquota: Holiday entitlement (quota) for users.
 - individualuseraccess: Permissions for individual users.
 - nonbusinessdays: Company-wide non-working days (e.g., holidays).
 - nonbusinessgroups: Groups of non-working days (e.g., holiday calendars).
 - users_access_customers_projects: User access to specific customers and projects.
 - users_access_services: User access to specific services.
 - customers: Customer records.
 - customers_count_projects: Number of projects per customer.
 - holidayscarry: Carried-over holiday balances.
 - overtimecarry: Carried-over overtime balances.
 - overtimereductions: Overtime reductions (corrections).
 - subprojects: Subdivisions of projects.
 - teams: Teams of users.
 - users: User records.
 - usersnonbusinessgroups: Assignment of users to nonbusiness groups.
 - absences: Absence records (e.g., vacation, sick leave).
 - lumpsumservices: Services billed as a lump sum.
 - projects: Project records.
 - projects_reports: Reports summarizing project activity.
 - services: Service records (types of work performed). """, json_response=True)

    def tool(self, flag: str = "default"):
        def decorator(func):
            #self.mcp.tool(*args, **kwargs)(func)
            self.collected_tools.append((func, flag))
            return func
        return decorator
    
    def register_tools(self, restricted: bool = False):
        for func, flag in self.collected_tools:
            if restricted and flag == "restricted":
                continue
            self.mcp.tool()(func)
    
mcp = ToolRestrictor()
