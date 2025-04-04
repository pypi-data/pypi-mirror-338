# This file serves all MaleoAccess's HTTP Client Services Results

from __future__ import annotations
from .blood_type import MaleoAccessHTTPClientBloodTypeServiceResults
from .gender import MaleoAccessHTTPClientGenderServiceResults
from .organization_role import MaleoAccessHTTPClientOrganizationRoleServiceResults
from .organization_type import MaleoAccessHTTPClientOrganizationTypeServiceResults
from .system_role import MaleoAccessHTTPClientSystemRoleServiceResults
from .user_type import MaleoAccessHTTPClientUserTypeServiceResults

class MaleoAccessHTTPClientServicesResults:
    BloodType = MaleoAccessHTTPClientBloodTypeServiceResults
    Gender = MaleoAccessHTTPClientGenderServiceResults
    OrganizationRole = MaleoAccessHTTPClientOrganizationRoleServiceResults
    OrganizationType = MaleoAccessHTTPClientOrganizationTypeServiceResults
    SystemRole = MaleoAccessHTTPClientSystemRoleServiceResults
    UserType = MaleoAccessHTTPClientUserTypeServiceResults

__all__ = [
    "MaleoAccessHTTPClientServicesResults",
    "MaleoAccessHTTPClientBloodTypeServiceResults",
    "MaleoAccessHTTPClientGenderServiceResults",
    "MaleoAccessHTTPClientOrganizationRoleServiceResults",
    "MaleoAccessHTTPClientOrganizationTypeServiceResults",
    "MaleoAccessHTTPClientSystemRoleServiceResults",
    "MaleoAccessHTTPClientUserTypeServiceResults"
]