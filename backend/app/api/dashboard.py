from fastapi import APIRouter

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/summary")
def get_dashboard_summary():
    return {
        "participants": 0,
        "competitions": 0,
        "organizations": 0,
        "users": 0,
    }
    