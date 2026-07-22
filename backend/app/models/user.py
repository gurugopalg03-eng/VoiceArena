from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
    )

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=True)

    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(20), nullable=True)

    password_hash = Column(String(255), nullable=False)

    role = Column(String(50), nullable=False, default="USER")

    is_active = Column(Boolean, nullable=False, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    organization = relationship("Organization", back_populates="users")