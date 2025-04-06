from __future__ import annotations
from maleo_core.models.base.transfers.parameters.service import BaseServiceParameters
from maleo_core.models.maleo_suite.maleo_access.transfers.parameters.general.organization import MaleoAccessOrganizationGeneralParameters

class MaleoAccessOrganizationServiceParameters:
    class GetQuery(MaleoAccessOrganizationGeneralParameters.Get, BaseServiceParameters.GetQuery): pass
    class Get(MaleoAccessOrganizationGeneralParameters.Get, BaseServiceParameters.Get): pass