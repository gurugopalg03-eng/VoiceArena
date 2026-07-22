from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import (
    create_new_user,
    delete_existing_user,
    get_all_users,
    get_user_by_id,
    update_existing_user,
)
from app.core.dependencies import get_current_user
from app.core.permissions import require_admin

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserResponse])
def get_users(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_all_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return get_user_by_id(db, user_id)
    except ValueError as ex:
        raise HTTPException(status_code=404, detail=str(ex))


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(
    user: UserCreate,
    current_user=Depends(require_admin),
    db: Session = Depends(get_db),
):
    try:
        # Temporary placeholder until JWT/Auth module
       return create_new_user(db, user)
    except ValueError as ex:
        raise HTTPException(status_code=400, detail=str(ex))


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
):
    try:
        return update_existing_user(db, user_id, user)
    except ValueError as ex:
        raise HTTPException(status_code=404, detail=str(ex))


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        delete_existing_user(db, user_id)
        return {"message": "User deleted successfully"}
    except ValueError as ex:
        raise HTTPException(status_code=404, detail=str(ex))