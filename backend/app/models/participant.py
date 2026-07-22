from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    mobile = Column(String(15), unique=True, nullable=False)