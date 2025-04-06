from maleo_core.clients.maleo_suite.maleo_access.http.manager import MaleoAccessHTTPClientManager
from maleo_core.models.base.transfers.parameters.general import BaseGeneralParameters
from maleo_core.models.base.transfers.results.clients.http.controller import BaseHTTPClientControllerResults
from maleo_core.models.maleo_suite.maleo_access.transfers.parameters.client.organization_type import MaleoAccessOrganizationTypeClientParameters
from maleo_core.models.maleo_suite.maleo_access.transfers.parameters.general.organization_type import MaleoAccessOrganizationTypeGeneralParameters

class MaleoAccessOrganizationTypeHTTPController:
    @staticmethod
    async def get_organization_types(
        parameters:MaleoAccessOrganizationTypeClientParameters.Get
    ) -> BaseHTTPClientControllerResults:
        """Fetch organization types from maleo-access"""
        async with MaleoAccessHTTPClientManager.get() as client:
            #* Define URL
            url = f"{MaleoAccessHTTPClientManager._base_url}/v1/organization-types/"

            query_parameters = MaleoAccessOrganizationTypeClientParameters.GetQuery.model_validate(parameters.model_dump())
            params = query_parameters.to_query_params()

            #* Get Response
            response = await client.get(url=url, params=params)
            return BaseHTTPClientControllerResults(response=response)

    @staticmethod
    async def get_organization_type(
        parameters:MaleoAccessOrganizationTypeGeneralParameters.GetSingle
    ) -> BaseHTTPClientControllerResults:
        """Fetch organization type from maleo-access"""
        async with MaleoAccessHTTPClientManager.get() as client:
            #* Define URL
            url = f"{MaleoAccessHTTPClientManager._base_url}/v1/organization-types/"
            if parameters.identifier == MaleoAccessOrganizationTypeGeneralParameters.UniqueIdentifiers.ID:
                url += f"{parameters.value}"
            else:
                url += f"{parameters.identifier.value}/{parameters.value}"

            #* Construct query parameters
            params = parameters.model_dump() if parameters else {}

            #* Get Response
            response = await client.get(url=url, params=params)
            return BaseHTTPClientControllerResults(response=response)

    @staticmethod
    async def status_update(
        organization_type_id:int,
        parameters:BaseGeneralParameters.StatusUpdate
    ) -> BaseHTTPClientControllerResults:
        """Update organization type's status"""
        async with MaleoAccessHTTPClientManager.get() as client:
            #* Define URL
            url = f"{MaleoAccessHTTPClientManager._base_url}/v1/organization-types/{organization_type_id}/status"

            #* Construct query parameters
            params = parameters.model_dump() if parameters else {}

            #* Get Response
            response = await client.get(url=url, params=params)
            return BaseHTTPClientControllerResults(response=response)