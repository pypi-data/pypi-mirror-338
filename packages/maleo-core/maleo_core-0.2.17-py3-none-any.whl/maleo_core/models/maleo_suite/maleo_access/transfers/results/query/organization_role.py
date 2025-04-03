from __future__ import annotations
from pydantic import Field
from typing import Optional
from maleo_core.models.base.transfers.results.services.query import BaseServiceQueryResults

class MaleoAccessOrganizationRoleQueryResults:
    class Get(BaseServiceQueryResults.Get):
        order:int = Field(..., ge=1, description="Organization Role's order")
        key:str = Field(..., max_length=20, description="Organization Role's key")
        name:str = Field(..., max_length=20, description="Organization Role's name")
        description:str = Field(..., max_length=50, description="Organization Role's description")
        icon:str = Field(..., max_length=20, description="Organization Role's icon")

    Fail = BaseServiceQueryResults.Fail

    class SingleData(BaseServiceQueryResults.SingleData):
        data:Optional[MaleoAccessOrganizationRoleQueryResults.Get]

    class MultipleData(BaseServiceQueryResults.MultipleData):
        data:list[MaleoAccessOrganizationRoleQueryResults.Get]