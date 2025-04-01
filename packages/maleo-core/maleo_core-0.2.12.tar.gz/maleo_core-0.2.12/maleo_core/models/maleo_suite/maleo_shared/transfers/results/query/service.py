from __future__ import annotations
from pydantic import Field
from typing import Optional
from uuid import UUID
from maleo_core.models.base.transfers.results.services.general import BaseServiceGeneralResults
from maleo_core.models.base.transfers.results.services.query import BaseServiceQueryResults

class MaleoSharedServiceQueryResults:
    class Get(BaseServiceQueryResults.Get):
        secret:UUID = Field(..., description="Service's secret")
        name:str = Field(..., description="Service's name")

    Fail = BaseServiceGeneralResults.Fail

    class SingleData(BaseServiceGeneralResults.SingleData):
        data:Optional[MaleoSharedServiceQueryResults.Get]

    class MultipleData(BaseServiceGeneralResults.MultipleData):
        data:list[MaleoSharedServiceQueryResults.Get]