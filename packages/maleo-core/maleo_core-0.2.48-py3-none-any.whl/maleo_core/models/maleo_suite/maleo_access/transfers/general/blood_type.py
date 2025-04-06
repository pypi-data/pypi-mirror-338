from __future__ import annotations
from pydantic import BaseModel, Field

class MaleoAccessBloodTypeGeneralTransfers:
    class Base(BaseModel):
        key:str = Field(..., max_length=2, description="Blood Type's key")
        name:str = Field(..., max_length=2, description="Blood Type's name")