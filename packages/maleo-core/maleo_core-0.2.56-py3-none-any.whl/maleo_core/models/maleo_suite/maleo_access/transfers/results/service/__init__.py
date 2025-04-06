# This file serves all MaleoAccess Services Results

from __future__ import annotations
from .blood_type import MaleoAccessBloodTypeServiceResults
from .gender import MaleoAccessGenderServiceResults
from .organization_role import MaleoAccessOrganizationRoleServiceResults
from .organization_type import MaleoAccessOrganizationTypeServiceResults
from .system_role import MaleoAccessSystemRoleServiceResults
from. user_type import MaleoAccessUserTypeServiceResults

class MaleoAccessServiceResults:
    BloodType = MaleoAccessBloodTypeServiceResults
    Gender = MaleoAccessGenderServiceResults
    OrganizationRole = MaleoAccessOrganizationRoleServiceResults
    OrganizationType = MaleoAccessOrganizationTypeServiceResults
    SystemRole = MaleoAccessSystemRoleServiceResults
    UserType = MaleoAccessUserTypeServiceResults

__all__ = [
    "MaleoAccessServiceResults",
    "MaleoAccessBloodTypeServiceResults",
    "MaleoAccessGenderServiceResults",
    "MaleoAccessOrganizationRoleServiceResults",
    "MaleoAccessOrganizationTypeServiceResults",
    "MaleoAccessSystemRoleServiceResults",
    "MaleoAccessUserTypeServiceResults"
]