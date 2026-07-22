from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class CompetitionBase(BaseModel):
    competition_name: str
    description: Optional[str] = None
    venue: str
    start_date: date
    end_date: date
    status: str = "Upcoming"


class CompetitionCreate(CompetitionBase):
    pass


class CompetitionUpdate(BaseModel):
    competition_name: Optional[str] = None
    description: Optional[str] = None
    venue: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[str] = None


class CompetitionResponse(CompetitionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        