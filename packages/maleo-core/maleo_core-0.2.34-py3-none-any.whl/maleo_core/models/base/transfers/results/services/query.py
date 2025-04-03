from __future__ import annotations
from datetime import datetime, date
from pydantic import field_validator, field_serializer
from pydantic_core.core_schema import FieldSerializationInfo
from typing import Optional, Any
from uuid import UUID
from maleo_core.models.base.transfers.results.general import BaseGeneralResults
from maleo_core.models.base.transfers.results.services.general import BaseServiceGeneralResults

class BaseServiceQueryResults:
    class Get(
        BaseGeneralResults.Status,
        BaseGeneralResults.Timestamp,
        BaseGeneralResults.Identifiers
    ):
        @field_validator('*', mode="before")
        def set_none(cls, values):
            if isinstance(values, str) and (values == "" or len(values) == 0):
                return None
            return values
        
        @field_serializer('*')
        def serialize_fields(self, value, info:FieldSerializationInfo) -> Any:
            """Serializes all unique-typed fields."""
            if isinstance(value, UUID):
                return str(value)
            if isinstance(value, datetime) or isinstance(value, date):
                return value.isoformat()
            return value

        class Config:
            from_attributes=True

    Fail = BaseServiceGeneralResults.Fail

    class SingleData(BaseServiceGeneralResults.SingleData):
        data:Optional[BaseServiceQueryResults.Get]

    class MultipleData(BaseServiceGeneralResults.MultipleData):
        data:list[BaseServiceQueryResults.Get]