from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.auth import create_access_token
from app.core.dependencies import get_current_user
from app.db.session import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.schemas.user import UserResponse
from app.services.user_service import authenticate_user, get_user_by_id

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(
        db,
        request.email,
        request.password,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email,
            "role": user.role,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get("/me", response_model=UserResponse)
def get_me(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_user_by_id(
        db,
        int(current_user["sub"]),
    )