from app.core.security import( 
get_password_hash,
verify_password
)

from sqlalchemy.orm import Session

from app.crud.user import (
    create_user,
    delete_user,
    get_user,
    get_user_by_email,
    get_users,
    update_user,
)

from app.schemas.user import UserCreate, UserUpdate


def create_new_user(db: Session, user: UserCreate):
    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        raise ValueError("Email already exists")

    password_hash = get_password_hash(user.password)

    return create_user(db, user, password_hash)


def get_all_users(db: Session):
    return get_users(db)


def get_user_by_id(db: Session, user_id: int):
    user = get_user(db, user_id)

    if not user:
        raise ValueError("User not found")

    return user


def update_existing_user(db: Session, user_id: int, user: UserUpdate):
    db_user = get_user(db, user_id)

    if not db_user:
        raise ValueError("User not found")

    return update_user(db, db_user, user)

def delete_existing_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)

    if not db_user:
        raise ValueError("User not found")

    delete_user(db, db_user)


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user