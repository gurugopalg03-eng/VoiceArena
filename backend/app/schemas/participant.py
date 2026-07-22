from pydantic import BaseModel, EmailStr


class ParticipantCreate(BaseModel):
    full_name: str
    email: EmailStr
    mobile: str


class ParticipantResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    mobile: str

    class Config:
        from_attributes = True