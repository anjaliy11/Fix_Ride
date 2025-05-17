from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str
    location: dict
    is_verified: bool = False
    is_admin: bool = False
