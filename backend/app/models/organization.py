from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)

    organization_name = Column(String(150), nullable=False)

    organization_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False
    )

    phone = Column(String(20), nullable=True)

    website = Column(String(200), nullable=True)

    address = Column(String(500), nullable=True)

    city = Column(String(100), nullable=True)

    state = Column(String(100), nullable=True)

    country = Column(String(100), nullable=True)

    logo_url = Column(String(500), nullable=True)

    subscription_plan = Column(
        String(50),
        nullable=False,
        default="FREE"
    )

    status = Column(
        String(20),
        nullable=False,
        default="ACTIVE"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    
    users = relationship(
    "User",
    back_populates="organization"
)