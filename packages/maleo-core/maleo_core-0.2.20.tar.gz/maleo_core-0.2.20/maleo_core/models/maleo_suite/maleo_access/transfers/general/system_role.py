from __future__ import annotations
from pydantic import BaseModel, Field

class MaleoAccessSystemRoleGeneralTransfers:
    class Base(BaseModel):
        order:int = Field(..., ge=1, description="System Role's order")
        key:str = Field(..., max_length=20, description="System Role's key")
        name:str = Field(..., max_length=20, description="System Role's name")
        description:str = Field(..., max_length=50, description="System Role's description")
        icon:str = Field(..., max_length=20, description="System Role's icon")