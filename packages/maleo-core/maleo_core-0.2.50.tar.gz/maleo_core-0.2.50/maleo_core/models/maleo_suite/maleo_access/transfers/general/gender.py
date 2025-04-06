from __future__ import annotations
from pydantic import BaseModel, Field

class MaleoAccessGenderGeneralTransfers:
    class Base(BaseModel):
        key:str = Field(..., max_length=15, description="Gender's key")
        name:str = Field(..., max_length=15, description="Gender's name")