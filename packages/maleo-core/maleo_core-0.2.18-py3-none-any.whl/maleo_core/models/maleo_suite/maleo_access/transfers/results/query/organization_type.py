from __future__ import annotations
from pydantic import Field
from typing import Optional
from maleo_core.models.base.transfers.results.services.query import BaseServiceQueryResults

class MaleoAccessOrganizationTypeQueryResults:
    class Get(BaseServiceQueryResults.Get):
        key:str = Field(..., max_length=2, description="Organization Type's key")
        name:str = Field(..., max_length=2, description="Organization Type's name")

    Fail = BaseServiceQueryResults.Fail

    class SingleData(BaseServiceQueryResults.SingleData):
        data:Optional[MaleoAccessOrganizationTypeQueryResults.Get]

    class MultipleData(BaseServiceQueryResults.MultipleData):
        data:list[MaleoAccessOrganizationTypeQueryResults.Get]