from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.participant import Participant
from app.models.competition import Competition
from app.models.organization import Organization
from app.models.user import User

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/summary")
def get_dashboard_summary(db: Session = Depends(get_db)):
    participants = db.query(Participant).count()
    competitions = db.query(Competition).count()
    organizations = db.query(Organization).count()
    users = db.query(User).count()

    return {
        "participants": participants,
        "competitions": competitions,
        "organizations": organizations,
        "users": users,
    }