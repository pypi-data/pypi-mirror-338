from __future__ import annotations
from enum import StrEnum
from pydantic import Field
from typing import Union
from uuid import UUID
from maleo_core.models.base.transfers.parameters.general import BaseGeneralParameters
from maleo_core.models.maleo_suite.maleo_access.transfers.general.blood_type import MaleoAccessBloodTypeGeneralTransfers

class MaleoAccessBloodTypeGeneralParameters:
    class UniqueIdentifiers(StrEnum):
        ID = "id"
        UUID = "uuid"
        KEY = "key"
        NAME = "name"

    class GetSingle(BaseGeneralParameters.GetSingle):
        identifier:MaleoAccessBloodTypeGeneralParameters.UniqueIdentifiers = Field(..., description="Identifier")
        value:Union[int, UUID, str] = Field(..., description="Value")

    CreateOrUpdate = MaleoAccessBloodTypeGeneralTransfers.Base

    class CheckUniqueExistence(BaseGeneralParameters.CheckUniqueExistence):
        field:MaleoAccessBloodTypeGeneralParameters.UniqueIdentifiers = Field(..., description="Field to be checked")

    UniqueFieldChecks = list[CheckUniqueExistence]