from sqlalchemy.orm import Session

from app.models.competition import Competition
from app.schemas.competition import CompetitionCreate


def create_competition(db: Session, competition: CompetitionCreate) -> Competition:
    db_competition = Competition(**competition.model_dump())
    db.add(db_competition)
    db.commit()
    db.refresh(db_competition)
    return db_competition

from typing import List

def get_all_competitions(db: Session) -> List[Competition]:
    return db.query(Competition).all()