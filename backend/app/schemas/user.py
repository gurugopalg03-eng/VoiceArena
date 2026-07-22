from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr
    phone: Optional[str] = None
    role: str = "USER"
    is_active: bool = True


class UserCreate(UserBase):
    organization_id: int
    password: str


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None


class UserResponse(UserBase):
    id: int
    organization_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True