from __future__ import annotations
from enum import StrEnum
from pydantic import BaseModel, Field
from typing import Union
from uuid import UUID
from maleo_core.models.base.transfers.parameters.general import BaseGeneralParameters
from maleo_core.models.maleo_suite.maleo_access.transfers.general.organization_type import MaleoAccessOrganizationTypeGeneralTransfers

class MaleoAccessOrganizationTypeGeneralParameters:
    class UniqueIdentifiers(StrEnum):
        ID = "id"
        UUID = "uuid"
        KEY = "key"
        NAME = "name"

    class GetSingle(BaseGeneralParameters.GetSingle):
        identifier:MaleoAccessOrganizationTypeGeneralParameters.UniqueIdentifiers = Field(..., description="Identifier")
        value:Union[int, UUID, str] = Field(..., description="Value")

    CreateOrUpdate = MaleoAccessOrganizationTypeGeneralTransfers.Base

    class CheckUniqueExistence(BaseGeneralParameters.CheckUniqueExistence):
        field:MaleoAccessOrganizationTypeGeneralParameters.UniqueIdentifiers = Field(..., description="Field to be checked")

    UniqueFieldChecks = list[CheckUniqueExistence]