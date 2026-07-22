from app.db.database import Base

# Import all models here so Alembic can discover them
from app.models.participant import Participant
from app.models.competition import Competition
from app.models.organization import Organization
from app.models.user import User