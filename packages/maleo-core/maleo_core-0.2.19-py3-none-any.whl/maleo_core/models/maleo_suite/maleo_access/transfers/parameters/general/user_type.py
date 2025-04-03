from __future__ import annotations
from enum import StrEnum
from pydantic import BaseModel, Field
from typing import Union
from uuid import UUID
from maleo_core.models.base.transfers.parameters.general import BaseGeneralParameters

class MaleoAccessUserTypeGeneralParameters:
    class Identifiers(StrEnum):
        ID = "id"
        UUID = "uuid"
        KEY = "key"
        NAME = "name"

    class GetSingle(BaseGeneralParameters.GetSingle):
        identifier:MaleoAccessUserTypeGeneralParameters.Identifiers = Field(..., description="Identifier")
        value:Union[int, UUID, str] = Field(..., description="Value")

    class CreateOrUpdate(BaseModel):
        key:str = Field(..., max_length=20, description="User Type's key")
        name:str = Field(..., max_length=20, description="User Type's name")