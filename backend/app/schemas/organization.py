from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from datetime import datetime


class OrganizationBase(BaseModel):
    organization_name: str
    organization_code: str
    email: EmailStr
    phone: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    logo_url: Optional[str] = None
    subscription_plan: str = "FREE"
    status: str = "ACTIVE"


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationUpdate(BaseModel):
    organization_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    logo_url: Optional[str] = None
    subscription_plan: Optional[str] = None
    status: Optional[str] = None


class OrganizationResponse(OrganizationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)