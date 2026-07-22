from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func

from app.db.database import Base


class Competition(Base):
    __tablename__ = "competitions"

    id = Column(Integer, primary_key=True, index=True)
    competition_name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    venue = Column(String(100), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False, default="Upcoming")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )