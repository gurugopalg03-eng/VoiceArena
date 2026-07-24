from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
import app.models

from app.api.participant import router as participant_router
from app.api.competition import router as competition_router
from app.api.organization import router as organization_router
from app.api.user import router as user_router
from app.api.auth import router as auth_router
from app.api.dashboard import router as dashboard_router

app = FastAPI(title="Voice Arena API")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(participant_router)
app.include_router(competition_router)
app.include_router(organization_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(dashboard_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Voice Arena",
        "version": "1.0"
    }