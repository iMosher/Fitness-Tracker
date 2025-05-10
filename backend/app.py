from fastapi import FastAPI
from backend.router import router as api_router

app = FastAPI(
    title="Fitness Tracker",
    summary="A fitness tracker API",
    version="0.0.1",
    docs_url="/swagger",
)

app.include_router(api_router, prefix="/api", tags=["api"])
