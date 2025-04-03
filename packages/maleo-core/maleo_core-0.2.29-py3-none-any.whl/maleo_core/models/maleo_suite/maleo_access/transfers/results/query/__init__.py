# This file serves all MaleoAccess's query results

from __future__ import annotations
from .blood_type import MaleoAccessBloodTypeQueryResults
from .gender import MaleoAccessGenderQueryResults
from .organization_role import MaleoAccessOrganizationRoleQueryResults
from .organization_type import MaleoAccessOrganizationTypeQueryResults
from .system_role import MaleoAccessSystemRoleQueryResults
from .user_type import MaleoAccessUserTypeQueryResults

class MaleoAccessQueryResults:
    BloodType = MaleoAccessBloodTypeQueryResults
    Gender = MaleoAccessGenderQueryResults
    OrganizationRole = MaleoAccessOrganizationRoleQueryResults
    OrganizationType = MaleoAccessOrganizationTypeQueryResults
    SystemRole = MaleoAccessSystemRoleQueryResults
    UserType = MaleoAccessUserTypeQueryResults

__all__ = [
    "MaleoAccessQueryResults",
    "MaleoAccessBloodTypeQueryResults",
    "MaleoAccessGenderQueryResults",
    "MaleoAccessOrganizationRoleQueryResults",
    "MaleoAccessOrganizationTypeQueryResults",
    "MaleoAccessSystemRoleQueryResults",
    "MaleoAccessUserTypeQueryResults"
]