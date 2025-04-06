from fastapi import status
from typing import Callable, Type, Union
from maleo_core.models.base.schemas.responses.general import BaseGeneralResponsesSchemas
from maleo_core.models.base.transfers.parameters.general import BaseGeneralParameters
from maleo_core.models.base.transfers.results.services.general import BaseServiceGeneralResults
from maleo_core.models.base.transfers.results.services.controllers.rest import BaseServiceRESTControllerResults

class BaseController:
    @staticmethod
    def check_unique_existence(
        check:BaseGeneralParameters.UniqueFieldCheck,
        get_single_parameters_class:Type[BaseGeneralParameters.GetSingle],
        get_single_function:Callable[[BaseGeneralParameters.GetSingle], BaseServiceRESTControllerResults],
        get_single_response_class:Type[BaseGeneralResponsesSchemas.SingleData],
        create_failed_response_class:Type[BaseGeneralResponsesSchemas.Fail],
        update_failed_response_class:Type[BaseGeneralResponsesSchemas.Fail]
    ) -> BaseServiceRESTControllerResults:
        """Generic helper function to check if a unique value exists in the database."""

        #* Return early if nullable and no new value
        if check.nullable and check.new_value is None:
            return BaseServiceRESTControllerResults(success=True, content=None)

        #* Return early if values are unchanged on update
        if check.operation == BaseGeneralParameters.OperationType.UPDATE and check.old_value == check.new_value:
            return BaseServiceRESTControllerResults(success=True, content=None)

        #* Prepare parameters to query for existing data
        get_single_parameters = get_single_parameters_class(identifier=check.field, value=check.new_value)

        #* Query the existing data using provided function
        existing_data_result:BaseServiceRESTControllerResults = get_single_function(parameters=get_single_parameters)
        if not existing_data_result.success:
            return existing_data_result

        controller_response = get_single_response_class.model_validate(existing_data_result.content)

        #* Handle case if duplicate is found
        if controller_response.data:
            description = f"External error: {check.field} of '{check.new_value}' already exists in the database"
            other = check.suggestion or f"Select another {check.field} value"
            if check.operation == BaseGeneralParameters.OperationType.CREATE:
                content = create_failed_response_class(description=description, other=other).model_dump()
            elif check.operation == BaseGeneralParameters.OperationType.UPDATE:
                content = update_failed_response_class(description=description, other=other).model_dump()

            return BaseServiceRESTControllerResults(success=False, content=content, status_code=status.HTTP_400_BAD_REQUEST)

        #* No duplicates found
        return BaseServiceRESTControllerResults(success=True, content=None)