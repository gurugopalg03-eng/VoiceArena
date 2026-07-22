from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.competition import CompetitionCreate, CompetitionResponse
from app.services.competition_service import create_competition_service, get_all_competitions_service

router = APIRouter(prefix="/competitions", tags=["Competitions"])


@router.post("/", response_model=CompetitionResponse)
def create_competition(
    competition: CompetitionCreate,
    db: Session = Depends(get_db),
):
    return create_competition_service(db, competition)

from typing import List

@router.get("/", response_model=list[CompetitionResponse])
def get_all_competitions(
    db: Session = Depends(get_db),
):
    return get_all_competitions_service(db)