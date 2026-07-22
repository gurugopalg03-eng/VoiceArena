from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.participant import Participant
from app.core.exceptions import (
    ParticipantAlreadyExistsException,
    ParticipantNotFoundException,
)


def create_participant(db: Session, participant):
    try:
        new_participant = Participant(
            full_name=participant.full_name,
            email=participant.email,
            mobile=participant.mobile,
        )

        db.add(new_participant)
        db.commit()
        db.refresh(new_participant)

        return new_participant

    except IntegrityError:
        db.rollback()
        raise ParticipantAlreadyExistsException()


def get_all_participants(db: Session):
    return db.query(Participant).all()


def update_participant(db: Session, participant_id, participant):

    existing_participant = (
        db.query(Participant)
        .filter(Participant.id == participant_id)
        .first()
    )

    if not existing_participant:
        raise ParticipantNotFoundException()

    try:
        existing_participant.full_name = participant.full_name
        existing_participant.email = participant.email
        existing_participant.mobile = participant.mobile

        db.commit()
        db.refresh(existing_participant)

        return existing_participant

    except IntegrityError:
        db.rollback()
        raise ParticipantAlreadyExistsException()


def delete_participant(db: Session, participant_id):

    participant = (
        db.query(Participant)
        .filter(Participant.id == participant_id)
        .first()
    )

    if not participant:
        raise ParticipantNotFoundException()

    db.delete(participant)
    db.commit()

    return {"message": "Participant deleted successfully"}