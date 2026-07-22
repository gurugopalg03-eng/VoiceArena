from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.auth import decode_access_token

security = HTTPBearer(
    bearerFormat="JWT",
    scheme_name="JWT Authentication"
)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
        )

    return payload


def require_role(*allowed_roles):
    def role_checker(current_user=Depends(get_current_user)):
        user_role = current_user.get("role")

        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="You don't have permission to perform this action.",
            )

        return current_user

    return role_checker