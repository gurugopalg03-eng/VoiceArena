from sqlalchemy.orm import Session

from app.crud.competition import create_competition, get_all_competitions
from app.schemas.competition import CompetitionCreate


def create_competition_service(
    db: Session,
    competition: CompetitionCreate,
):
    return create_competition(db, competition)

from typing import List
from app.models.competition import Competition

def get_all_competitions_service(db: Session) -> List[Competition]:
    return get_all_competitions(db)