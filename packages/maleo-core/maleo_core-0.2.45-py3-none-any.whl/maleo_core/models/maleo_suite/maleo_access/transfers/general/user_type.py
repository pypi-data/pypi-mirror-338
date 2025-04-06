from __future__ import annotations
from pydantic import BaseModel, Field

class MaleoAccessUserTypeGeneralTransfers:
    class Base(BaseModel):
        key:str = Field(..., max_length=20, description="User Type's key")
        name:str = Field(..., max_length=20, description="User Type's name")