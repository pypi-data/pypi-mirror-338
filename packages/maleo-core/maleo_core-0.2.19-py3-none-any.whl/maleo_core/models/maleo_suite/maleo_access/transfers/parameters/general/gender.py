from __future__ import annotations
from enum import StrEnum
from pydantic import Field
from typing import Union
from uuid import UUID
from maleo_core.models.base.transfers.parameters.general import BaseGeneralParameters

class MaleoAccessGenderGeneralParameters:
    class Identifiers(StrEnum):
        ID = "id"
        UUID = "uuid"
        KEY = "key"
        NAME = "name"

    class GetSingle(BaseGeneralParameters.GetSingle):
        identifier:MaleoAccessGenderGeneralParameters.Identifiers = Field(..., description="Identifier")
        value:Union[int, UUID, str] = Field(..., description="Value")