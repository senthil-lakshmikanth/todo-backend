from fastapi import FastAPI
from .database import engine, Base
from . import models
from .auth import router as auth_router
from .tasks import router as tasks_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(tasks_router)

@app.get("/")
def home():
    return {"message": "To-Do Tracker Backend Running"}
