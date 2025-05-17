from pydantic import BaseModel
from typing import List

class ServiceType(BaseModel):
    name: str
    description: str
    estimated_cost: float
    estimated_time: str
    category: str
    priority: str
    mechanics_available: List[str]
