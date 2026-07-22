from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, user: UserCreate, password_hash: str):
    db_user = User(
        organization_id=user.organization_id,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        phone=user.phone,
        password_hash=password_hash,
        role=user.role,
        is_active=user.is_active,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(db: Session, db_user: User, user: UserUpdate):
    for key, value in user.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db: Session, db_user: User):
    db.delete(db_user)
    db.commit()
    