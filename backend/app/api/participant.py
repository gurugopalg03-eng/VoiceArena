from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.participant import (
    ParticipantCreate,
    ParticipantResponse,
)

from app.services.participant_service import (
    create_participant,
    get_all_participants,
    update_participant,
    delete_participant,
)

router = APIRouter(
    prefix="/participants",
    tags=["Participants"]
)


@router.post("/", response_model=ParticipantResponse)
def add_participant(
    participant: ParticipantCreate,
    db: Session = Depends(get_db)
):
    return create_participant(db, participant)


@router.get("/", response_model=list[ParticipantResponse])
def fetch_participants(
    db: Session = Depends(get_db)
):
    return get_all_participants(db)


@router.put("/{participant_id}", response_model=ParticipantResponse)
def edit_participant(
    participant_id: int,
    participant: ParticipantCreate,
    db: Session = Depends(get_db)
):
    return update_participant(
        db,
        participant_id,
        participant
    )


@router.delete("/{participant_id}")
def remove_participant(
    participant_id: int,
    db: Session = Depends(get_db)
):
    return delete_participant(
        db,
        participant_id
    )