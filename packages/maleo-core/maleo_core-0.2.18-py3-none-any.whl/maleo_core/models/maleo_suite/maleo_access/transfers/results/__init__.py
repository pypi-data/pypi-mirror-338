# This file serves all MaleoAccess's Results

from __future__ import annotations
from .client import MaleoSharedClientResults
from .service import MaleoAccessServiceResults
from .query import MaleoAccessQueryResults

class MaleoAccessResults:
    Client = MaleoSharedClientResults
    Service = MaleoAccessServiceResults
    Query = MaleoAccessQueryResults

__all__ = [
    "MaleoAccessResults",
    "MaleoSharedClientResults",
    "MaleoAccessServiceResults",
    "MaleoAccessQueryResults"
]