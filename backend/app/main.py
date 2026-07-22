from fastapi import FastAPI

from app.api.participant import router as participant_router
from app.api.competition import router as competition_router
from app.api.organization import router as organization_router 
from app.api.user import router as user_router
from app.api.auth import router as auth_router

app = FastAPI(title="Voice Arena API")

app.include_router(participant_router)
app.include_router(competition_router)
app.include_router(organization_router)
app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Voice Arena",
        "version": "1.0"
    }