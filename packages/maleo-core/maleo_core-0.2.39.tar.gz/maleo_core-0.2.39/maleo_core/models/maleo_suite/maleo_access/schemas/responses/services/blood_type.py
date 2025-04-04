from __future__ import annotations
from fastapi import status
from maleo_core.models.base.schemas.responses.general import BaseGeneralResponsesSchemas
from maleo_core.models.base.schemas.responses.service import BaseServiceResponsesSchemas
from maleo_core.models.maleo_suite.maleo_access.transfers.results.query.blood_type import MaleoAccessBloodTypeQueryResults

class MaleoAccessBloodTypeServiceResponsesSchemas:
    #* ----- ----- Response ----- ----- *#
    class NotFoundResponse(BaseGeneralResponsesSchemas.Fail):
        code:str = "ACC-BLT-001"
        message:str = "No blood type(s) found"
        description:str = "External error: No blood type(s) found in database acording to given parameter(s)"
        other:str = "Ensure parameter(s) are correct"

    class GetMultipleResponse(BaseServiceResponsesSchemas.MultipleData):
        code:str = "ACC-BLT-002"
        message:str = "Blood types found"
        description:str = "Requested blood types found in database"
        data:list[MaleoAccessBloodTypeQueryResults.Get]

    class GetSuccessResponse(BaseGeneralResponsesSchemas.SingleData):
        code:str = "ACC-BLT-003"
        message:str = "Blood type found"
        description:str = "Requested blood type found in database"
        data:MaleoAccessBloodTypeQueryResults.Get

    class CheckFailedResponse(BaseGeneralResponsesSchemas.Fail):
        code:str = "ACC-BLT-004"

    class CreateSuccessResponse(BaseGeneralResponsesSchemas.SingleData):
        code:str = "ACC-BLT-005"
        message:str = "Succesfully created new blood type"
        description:str = "A new blood type is created with data provided on request"
        data:MaleoAccessBloodTypeQueryResults.Get

    class CreateFailedResponse(BaseGeneralResponsesSchemas.Fail):
        code:str = "ACC-BLT-006"
        message:str = "Failed creating blood type"

    class UpdateSuccessResponse(BaseGeneralResponsesSchemas.SingleData):
        code:str = "ACC-BLT-007"
        message:str = "Succesfully updated blood type"
        data:MaleoAccessBloodTypeQueryResults.Get

    class UpdateFailedResponse(BaseGeneralResponsesSchemas.Fail):
        code:str = "ACC-BLT-008"
        message:str = "Failed updating blood type"

    class StatusUpdateResponse(BaseGeneralResponsesSchemas.SingleData):
        code:str = "ACC-BLT-009"

    #* ----- ----- Responses Class ----- ----- *#
    not_found_responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "No blood types found Response",
            "model": NotFoundResponse
        }
    }

    check_responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Check failed response",
            "model": CheckFailedResponse
        },
        **not_found_responses,
        **BaseGeneralResponsesSchemas.other_responses
    }

    get_single_responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Get blood type failed response",
            "model": CheckFailedResponse
        },
        **not_found_responses,
        **BaseGeneralResponsesSchemas.other_responses
    }

    create_responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Create failed response",
            "model": CreateFailedResponse
        },
        **BaseGeneralResponsesSchemas.other_responses
    }

    update_responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Update failed response",
            "model": UpdateFailedResponse
        },
        **not_found_responses,
        **BaseGeneralResponsesSchemas.other_responses
    }