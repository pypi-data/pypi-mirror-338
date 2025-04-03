# This file serves all MaleoAccess's HTTP Client Services Results

from __future__ import annotations
from .blood_type import MaleoSharedHTTPClientBloodTypeServiceResults
from .gender import MaleoSharedHTTPClientGenderServiceResults
from .organization_role import MaleoSharedHTTPClientOrganizationRoleServiceResults
from .organization_type import MaleoSharedHTTPClientOrganizationTypeServiceResults
from .system_role import MaleoSharedHTTPClientSystemRoleServiceResults
from .user_type import MaleoSharedHTTPClientUserTypeServiceResults

class MaleoAccessHTTPClientServicesResults:
    BloodType = MaleoSharedHTTPClientBloodTypeServiceResults
    Gender = MaleoSharedHTTPClientGenderServiceResults
    OrganizationRole = MaleoSharedHTTPClientOrganizationRoleServiceResults
    OrganizationType = MaleoSharedHTTPClientOrganizationTypeServiceResults
    SystemRole = MaleoSharedHTTPClientSystemRoleServiceResults
    UserType = MaleoSharedHTTPClientUserTypeServiceResults

__all__ = [
    "MaleoAccessHTTPClientServicesResults",
    "MaleoSharedHTTPClientBloodTypeServiceResults",
    "MaleoSharedHTTPClientGenderServiceResults",
    "MaleoSharedHTTPClientOrganizationRoleServiceResults",
    "MaleoSharedHTTPClientOrganizationTypeServiceResults",
    "MaleoSharedHTTPClientSystemRoleServiceResults",
    "MaleoSharedHTTPClientUserTypeServiceResults"
]