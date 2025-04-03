from __future__ import annotations
from datetime import datetime, date
from pydantic import BaseModel, Field, field_serializer
from pydantic_core.core_schema import FieldSerializationInfo
from typing import Literal, Optional, Union, Any
from uuid import UUID
from maleo_core.models.base.general import BaseGeneralModels
from maleo_core.models.base.transfers.parameters.general import BaseGeneralParameters

class BaseGeneralResults:
    class Identifiers(BaseModel):
        id:int = Field(..., ge=1, description="Data's ID, must be >= 1.")
        uuid:UUID = Field(..., description="Data's UUID.")

        @field_serializer('uuid')
        def serialize_uuid(self, value:UUID, info:FieldSerializationInfo) -> str:
            """Serializes UUID to a hex string."""
            return str(value)

    class Timestamp(BaseModel):
        created_at:datetime = Field(..., description="Data's created_at timestamp")
        updated_at:datetime = Field(..., description="Data's updated_at timestamp")

        @field_serializer('created_at', 'updated_at')
        def serialize_timestamps(self, value:Union[datetime, date], info:FieldSerializationInfo) -> str:
            """Serializes datetime/date fields to ISO format."""
            return value.isoformat()

    class Status(BaseModel):
        is_deleted:bool = Field(..., description="Data's deletion status.")
        is_active:bool = Field(..., description="Data's active status.")
        status:BaseGeneralModels.StatusType = Field(..., description="Data's status")

    #* ----- ----- ----- Base ----- ----- ----- *#
    class Base(BaseModel):
        success:bool = Field(..., description="Success status")
        message:Optional[str] = Field(None, description="Optional message")
        description:Optional[str] = Field(None, description="Optional description")

    #* ----- ----- ----- Derived ----- ----- ----- *#
    class Fail(Base):
        success:Literal[False] = Field(False, description="Success status")
        other:Optional[Any] = Field(None, description="Optional other information")

    class SingleData(Base):
        success:Literal[True] = Field(True, description="Success status")
        data:Any = Field(..., description="Fetched data")
        other:Optional[Any] = Field(None, description="Optional other information")

    class MultipleData(
        Base,
        BaseGeneralModels.SimplePagination
    ):
        total_data:int = Field(..., description="Total data count")
        success:Literal[True] = Field(True, description="Success status")
        data:list[Any] = Field(..., description="Paginated data")
        pagination:BaseGeneralModels.ExtendedPagination = Field(..., description="Pagination metadata")
        other:Optional[Any] = Field(None, description="Optional other information")

    class StatusUpdateResponse(BaseModel):
        message:str = Field(..., "Status update response message")
        update_description:str = Field(..., "Status update on update response description")
        maintain_description:str = Field(..., "Status update on maintain response description")

    StatusUpdateResponseMappings = dict[BaseGeneralParameters.StatusUpdateAction, StatusUpdateResponse]

    @staticmethod
    def generate_status_update_response(name:str, action:BaseGeneralParameters.StatusUpdateAction) -> StatusUpdateResponse:
        status_update_response_mappings:BaseGeneralResults.StatusUpdateResponseMappings = {
            BaseGeneralParameters.StatusUpdateAction.DELETE: BaseGeneralResults.StatusUpdateResponse(
                message=f"{name} successfully deleted",
                update_description=f"{name}'s `is_deleted` status changed to `true`",
                maintain_description=f"{name} is already deleted, no data are changed"
            ),
            BaseGeneralParameters.StatusUpdateAction.RESTORE: BaseGeneralResults.StatusUpdateResponse(
                message=f"{name} successfully restored",
                update_description=f"{name}'s `is_deleted` status changed to `false`",
                maintain_description=f"{name} is already restored, no data are changed"
            ),
            BaseGeneralParameters.StatusUpdateAction.DEACTIVATE: BaseGeneralResults.StatusUpdateResponse(
                message=f"{name} successfully deactivated",
                update_description=f"{name}'s `is_active` status changed to `false`",
                maintain_description=f"{name} is already inactive, no data are changed"
            ),
            BaseGeneralParameters.StatusUpdateAction.ACTIVATE: BaseGeneralResults.StatusUpdateResponse(
                message=f"{name} successfully activated",
                update_description=f"{name}'s `is_active` status changed to `true`",
                maintain_description=f"{name} is already active, no data are changed"
            ),
        }
        return status_update_response_mappings.get(action)