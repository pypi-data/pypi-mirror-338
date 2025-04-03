# This file serves all MaleoAccess's General Transfers

from __future__ import annotations
from .organization_role import MaleoAccessOrganizationRoleGeneralTransfers
from .system_role import MaleoAccessSystemRoleGeneralTransfers

class MaleoAccessGeneralTransfers:
    OrganizationRole = MaleoAccessOrganizationRoleGeneralTransfers
    SystemRole = MaleoAccessSystemRoleGeneralTransfers

__all__ = [
    "MaleoAccessGeneralTransfers",
    "MaleoAccessOrganizationRoleGeneralTransfers",
    "MaleoAccessSystemRoleGeneralTransfers"
]