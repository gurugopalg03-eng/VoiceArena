from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None = None
    organization_id: int
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"