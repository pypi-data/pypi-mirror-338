from __future__ import annotations
from fastapi import status
from maleo_core.models.base.schemas.responses.general import BaseGeneralResponsesSchemas
from maleo_core.models.base.schemas.responses.service import BaseServiceResponsesSchemas
from maleo_core.models.maleo_suite.maleo_access.transfers.results.query.user_type import MaleoAccessUserTypeQueryResults

class MaleoAccessUserTypeServiceResponsesSchemas:
    #* ----- ----- Response ----- ----- *#
    class NotFoundResponse(BaseGeneralResponsesSchemas.Fail):
        code:str = "ACC-UST-001"
        message:str = "No user type(s) found"
        description:str = "External error: No user type(s) found in database acording to given parameter(s)"
        other:str = "Ensure parameter(s) are correct"

    class GetMultipleResponse(BaseServiceResponsesSchemas.MultipleData):
        code:str = "ACC-UST-002"
        message:str = "User types found"
        description:str = "Requested user types found in database"
        data:list[MaleoAccessUserTypeQueryResults.Get]

    class GetSuccessResponse(BaseGeneralResponsesSchemas.SingleData):
        code:str = "ACC-UST-003"
        message:str = "User type found"
        description:str = "Requested user type found in database"
        data:MaleoAccessUserTypeQueryResults.Get

    class CheckFailedResponse(BaseGeneralResponsesSchemas.Fail):
        code:str = "ACC-UST-004"

    class CreateSuccessResponse(BaseGeneralResponsesSchemas.SingleData):
        code:str = "ACC-SYR-005"
        message:str = "Succesfully created new user type"
        description:str = "A new user type is created with data provided on request"
        data:MaleoAccessUserTypeQueryResults.Get

    class CreateFailedResponse(BaseGeneralResponsesSchemas.Fail):
        code:str = "ACC-SYR-006"
        message:str = "Failed creating user type"

    class UpdateSuccessResponse(BaseGeneralResponsesSchemas.SingleData):
        code:str = "ACC-SYR-007"
        message:str = "Succesfully updated user type"
        data:MaleoAccessUserTypeQueryResults.Get

    class UpdateFailedResponse(BaseGeneralResponsesSchemas.Fail):
        code:str = "ACC-SYR-008"
        message:str = "Failed updating user type"

    class StatusUpdateResponse(BaseGeneralResponsesSchemas.SingleData):
        code:str = "ACC-UST-009"

    #* ----- ----- Responses Class ----- ----- *#
    not_found_responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "No user types found Response",
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
            "description": "Get user type failed response",
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