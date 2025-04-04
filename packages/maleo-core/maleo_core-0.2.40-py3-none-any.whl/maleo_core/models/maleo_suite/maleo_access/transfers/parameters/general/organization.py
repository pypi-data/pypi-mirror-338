from __future__ import annotations
from enum import StrEnum
from pydantic import BaseModel, Field
from typing import Optional, Union
from uuid import UUID
from maleo_core.models.base.transfers.parameters.general import BaseGeneralParameters

class MaleoAccessOrganizationGeneralParameters:
    class ExpandableFields(StrEnum):
        TYPE = "organization_type"
        PARENT = "parent_organization"
        CHILD = "child_organizations"

    expandable_fields:set[ExpandableFields] = {
        ExpandableFields.TYPE,
        ExpandableFields.PARENT,
        ExpandableFields.CHILD
    }

    class Expand(BaseModel):
        expand:list[MaleoAccessOrganizationGeneralParameters.ExpandableFields] = Field([], description="Expanded field(s)")

    class StatusUpdate(Expand, BaseGeneralParameters.StatusUpdate): pass

    class UniqueIdentifiers(StrEnum):
        ID = "id"
        UUID = "uuid"
        KEY = "key"
        NAME = "name"

    class GetSingle(BaseGeneralParameters.GetSingle):
        identifier:MaleoAccessOrganizationGeneralParameters.UniqueIdentifiers = Field(..., description="Identifier")
        value:Union[int, UUID, str] = Field(..., description="Value")

    class BaseGet(BaseModel):
        is_root:Optional[bool] = Field(None, description="Filter organizations based on whether it's a root.")
        is_parent:Optional[bool] = Field(None, description="Filter organizations based on whether it's a parent.")
        is_child:Optional[bool] = Field(None, description="Filter organizations based on whether it's a child.")
        is_leaf:Optional[bool] = Field(None, description="Filter organizations based on whether it's a leaf.")

    class BaseCreateOrUpdate(BaseModel):
        organization_type_id:int = Field(1, ge=1, description="Organization's type id")
        parent_organization_id:Optional[int] = Field(None, ge=1, description="Parent organization's id")
        key:str = Field(..., max_length=255, description="Organization's key")
        name:str = Field(..., max_length=255, description="Organization's name")

    class CreateOrUpdate(Expand): pass