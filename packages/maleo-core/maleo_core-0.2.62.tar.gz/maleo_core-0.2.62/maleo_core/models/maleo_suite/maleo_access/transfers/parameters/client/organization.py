from __future__ import annotations
from maleo_core.models.base.transfers.parameters.client import BaseClientParameters
from maleo_core.models.maleo_suite.maleo_access.transfers.parameters.general.organization import MaleoAccessOrganizationGeneralParameters

class MaleoAccessOrganizationClientParameters:
    class Get(MaleoAccessOrganizationGeneralParameters.BaseGet, BaseClientParameters.Get): pass
    class GetQuery(MaleoAccessOrganizationGeneralParameters.BaseGet, BaseClientParameters.GetQuery): pass