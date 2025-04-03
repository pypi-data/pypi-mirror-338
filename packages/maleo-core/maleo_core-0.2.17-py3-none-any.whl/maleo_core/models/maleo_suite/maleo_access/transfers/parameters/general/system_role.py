from __future__ import annotations
from enum import StrEnum
from pydantic import BaseModel, Field
from typing import Optional, Union
from uuid import UUID
from maleo_core.models.base.transfers.parameters.general import BaseGeneralParameters

class MaleoAccessSystemRoleGeneralParameters:
    class Identifiers(StrEnum):
        ID = "id"
        UUID = "uuid"
        KEY = "key"
        NAME = "name"

    class GetSingle(BaseGeneralParameters.GetSingle):
        identifier:MaleoAccessSystemRoleGeneralParameters.Identifiers = Field(..., description="Identifier")
        value:Union[int, UUID, str] = Field(..., description="Value")