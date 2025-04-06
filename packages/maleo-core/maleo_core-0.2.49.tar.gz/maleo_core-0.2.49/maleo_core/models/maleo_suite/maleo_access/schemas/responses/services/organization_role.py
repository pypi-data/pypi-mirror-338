from __future__ import annotations
from fastapi import status
from maleo_core.models.base.schemas.responses.general import BaseGeneralResponsesSchemas
from maleo_core.models.base.schemas.responses.service import BaseServiceResponsesSchemas
from maleo_core.models.maleo_suite.maleo_access.transfers.results.query.organization_role import MaleoAccessOrganizationRoleQueryResults

class MaleoAccessOrganizationRoleServiceResponsesSchemas:
    #* ----- ----- Response ----- ----- *#
    class NotFoundResponse(BaseGeneralResponsesSchemas.Fail):
        code:str = "ACC-OGR-001"
        message:str = "No organization role(s) found"
        description:str = "External error: No organization role(s) found in database acording to given parameter(s)"
        other:str = "Ensure parameter(s) are correct"

    class GetMultipleResponse(BaseServiceResponsesSchemas.MultipleData):
        code:str = "ACC-OGR-002"
        message:str = "Organization roles found"
        description:str = "Requested organization roles found in database"
        data:list[MaleoAccessOrganizationRoleQueryResults.Get]

    class GetSuccessResponse(BaseGeneralResponsesSchemas.SingleData):
        code:str = "ACC-OGR-003"
        message:str = "Organization role found"
        description:str = "Requested organization role found in database"
        data:MaleoAccessOrganizationRoleQueryResults.Get

    class CheckFailedResponse(BaseGeneralResponsesSchemas.Fail):
        code:str = "ACC-OGR-004"

    class CreateSuccessResponse(BaseGeneralResponsesSchemas.SingleData):
        code:str = "ACC-OGR-005"
        message:str = "Succesfully created new organization role"
        description:str = "A new organization role is created with data provided on request"
        data:MaleoAccessOrganizationRoleQueryResults.Get

    class CreateFailedResponse(BaseGeneralResponsesSchemas.Fail):
        code:str = "ACC-OGR-006"
        message:str = "Failed creating organization role"

    class UpdateSuccessResponse(BaseGeneralResponsesSchemas.SingleData):
        code:str = "ACC-OGR-007"
        message:str = "Succesfully updated organization role"
        data:MaleoAccessOrganizationRoleQueryResults.Get

    class UpdateFailedResponse(BaseGeneralResponsesSchemas.Fail):
        code:str = "ACC-OGR-008"
        message:str = "Failed updating organization role"

    class StatusUpdateResponse(BaseGeneralResponsesSchemas.SingleData):
        code:str = "ACC-OGR-009"

    #* ----- ----- Responses Class ----- ----- *#
    not_found_responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "No organization roles found Response",
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
            "description": "Get organization role failed response",
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