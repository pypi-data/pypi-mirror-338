from __future__ import annotations
from pydantic import Field
from typing import Optional
from maleo_core.models.base.transfers.results.services.query import BaseServiceQueryResults

class MaleoAccessGenderQueryResults:
    class Get(BaseServiceQueryResults.Get):
        key:str = Field(..., max_length=2, description="Gender's key")
        name:str = Field(..., max_length=2, description="Gender's name")

    Fail = BaseServiceQueryResults.Fail

    class SingleData(BaseServiceQueryResults.SingleData):
        data:Optional[MaleoAccessGenderQueryResults.Get]

    class MultipleData(BaseServiceQueryResults.MultipleData):
        data:list[MaleoAccessGenderQueryResults.Get]