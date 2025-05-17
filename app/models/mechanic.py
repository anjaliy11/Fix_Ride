from pydantic import BaseModel
from typing import List, Dict

class Mechanic(BaseModel):
    name: str
    phone: str
    email: str
    location: Dict[str, float]
    experience: int
    expertise: List[str]
    availability: str
    rating: float
    total_jobs: int
    verified: bool