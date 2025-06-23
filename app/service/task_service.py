from typing import List
from uuid import UUID

from fastapi import HTTPException, status
from app.model import Task
from app.schema import TaskCreate, TaskUpdate, TaskResponse
from sqlalchemy.orm import Session

def create(data: TaskCreate, db: Session) -> TaskResponse:
    new_task = Task(**data.model_dump())
    db.add(new_task)
    db.commit() 
    db.refresh(new_task)
    return new_task

def get_all(db: Session) -> List[TaskResponse]:
    return db.query(Task).order_by(Task.create_at.asc()).all()

def update(task_id: UUID, task_data: TaskUpdate, db: Session) -> TaskResponse:
    task_query = db.query(Task).filter(Task.id == task_id)
    if not task_query.first():
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )
    task_query.update(task_data.model_dump(), synchronize_session=False)
    db.commit()
    return task_query.first()

def delete(task_id: UUID, db: Session):
    task_query = db.query(Task).filter(Task.id == task_id)
    if not task_query.first():
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )
    task_query.delete(synchronize_session=False)
    db.commit()
    
def update_status(task_id: UUID, db: Session) -> TaskResponse:
    task_query = db.query(Task).filter(Task.id == task_id)
    task = task_query.first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    task_query.update({"is_completed": not task.is_completed}, synchronize_session=False)
    db.commit()
    return task_query.first()