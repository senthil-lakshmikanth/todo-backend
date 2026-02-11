import os
from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.auth import router as auth_router
from app.tasks import router as tasks_router

CREATE_TABLES = os.getenv("CREATE_TABLES", "false").lower() in ("1", "true", "yes")
if CREATE_TABLES:
    Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(tasks_router)

@app.get("/")
def home():
    return {"message": "To-Do Tracker Backend Running"}