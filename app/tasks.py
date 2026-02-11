from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from pydantic import BaseModel

from .database import get_db
from . import models
from .auth import get_current_user

# -------------------------------
# Pydantic Schemas for Tasks
# -------------------------------
class TaskCreate(BaseModel):
    title: str
    description: str = None
    due_date: datetime = None

class TaskUpdate(BaseModel):
    title: str = None
    description: str = None
    due_date: datetime = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: str = None
    due_date: datetime = None
    created_at: datetime

    class Config:
        from_attributes = True

# -------------------------------
# Router & DB Dependency
# -------------------------------
router = APIRouter(prefix="/tasks", tags=["Tasks"])
# -------------------------------
# CRUD Routes
# -------------------------------

# 1️⃣ Create Task
@router.post("/", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        user_id=current_user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# 2️⃣ Get All Tasks for Current User
@router.get("/", response_model=List[TaskOut])
def get_tasks(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    tasks = db.query(models.Task).filter(models.Task.user_id == current_user.id).all()
    return tasks

# 3️⃣ Get Single Task by ID
@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.user_id == current_user.id
    ).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

# 4️⃣ Update Task
@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.user_id == current_user.id
    ).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.due_date is not None:
        task.due_date = task_update.due_date

    db.commit()
    db.refresh(task)
    return task

# 5️⃣ Delete Task
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.user_id == current_user.id
    ).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    db.delete(task)
    db.commit()
    return
