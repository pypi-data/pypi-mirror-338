from __future__ import annotations
from enum import StrEnum
from pydantic import BaseModel, Field
from typing import Optional, Union
from uuid import UUID
from maleo_core.models.base.general import BaseGeneralModels

class BaseGeneralParameters:
    class Expand(BaseModel):
        expand:list[str] = Field([], description="Expanded field(s)")

    class StatusUpdateAction(StrEnum):
        ACTIVATE = "activate"
        DEACTIVATE = "deactivate"
        RESTORE = "restore"
        DELETE = "delete"

    class StatusUpdate(BaseModel):
        action:BaseGeneralParameters.StatusUpdateAction = Field(..., description="Status update's action to be executed")

    class Statuses(BaseModel):
        statuses:Optional[list[BaseGeneralModels.StatusType]] = Field(None, description="Data's status")

    class Search(BaseModel):
        search:Optional[str] = Field(None, description="Search parameter string.")

    class Sorts(BaseModel):
        sort:list[str] = Field(["id.asc"], description="Sorting columns in 'column_name.asc' or 'column_name.desc' format.")

    class Filters(BaseModel):
        filter:list[str] = Field([], description="Filters for date range, e.g. 'created_at|from::<ISO_DATETIME>|to::<ISO_DATETIME>'.")

    class SortColumns(BaseModel):
        sort_columns:list[BaseGeneralModels.SortColumn] = Field([BaseGeneralModels.SortColumn(name="id", order=BaseGeneralModels.SortOrder.ASC)], description="List of columns to be sorted")

    class DateFilters(BaseModel):
        date_filters:list[BaseGeneralModels.DateFilter] = Field([], description="Date filters to be applied")

    class Identifiers(StrEnum):
        ID = "id"
        UUID = "uuid"

    class GetSingle(Statuses):
        identifier:BaseGeneralParameters.Identifiers = Field(..., description="Identifier")
        value:Union[int, UUID] = Field(..., description="Value")

    status_update_criterias:dict[
        BaseGeneralParameters.StatusUpdateAction,
        Optional[list[BaseGeneralModels.StatusType]]
    ] = {
        StatusUpdateAction.DELETE: None,
        StatusUpdateAction.RESTORE: None,
        StatusUpdateAction.DEACTIVATE: [
            BaseGeneralModels.StatusType.INACTIVE,
            BaseGeneralModels.StatusType.ACTIVE,
        ],
        StatusUpdateAction.ACTIVATE: [
            BaseGeneralModels.StatusType.INACTIVE,
            BaseGeneralModels.StatusType.ACTIVE,
        ]
    }

    class StatusUpdateResponse(BaseModel):
        message:str = Field(..., "Status update response message")
        update_description:str = Field(..., "Status update on update response description")
        maintain_description:str = Field(..., "Status update on maintain response description")

    StatusUpdateResponseMappings:dict[BaseGeneralParameters.StatusUpdateAction, StatusUpdateResponse]