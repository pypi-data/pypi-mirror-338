from __future__ import annotations
from pydantic import BaseModel, Field

class MaleoAccessOrganizationRoleGeneralTransfers:
    class Base(BaseModel):
        order:int = Field(..., ge=1, description="Organization Role's order")
        key:str = Field(..., max_length=20, description="Organization Role's key")
        name:str = Field(..., max_length=20, description="Organization Role's name")
        description:str = Field(..., max_length=50, description="Organization Role's description")
        icon:str = Field(..., max_length=20, description="Organization Role's icon")