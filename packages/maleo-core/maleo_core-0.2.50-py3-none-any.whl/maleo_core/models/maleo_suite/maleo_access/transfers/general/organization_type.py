from __future__ import annotations
from pydantic import BaseModel, Field

class MaleoAccessOrganizationTypeGeneralTransfers:
    class Base(BaseModel):
        key:str = Field(..., max_length=20, description="Organization Type's key")
        name:str = Field(..., max_length=20, description="Organization Type's name")