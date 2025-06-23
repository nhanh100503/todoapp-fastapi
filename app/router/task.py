from uuid import UUID
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.schema import TaskCreate, TaskResponse, TaskUpdate
from app.database import get_db
from app.service import task_service

router = APIRouter(
    prefix="/task",
    tags=['Task']
)

@router.post("/create", response_model=TaskResponse)
async def create(task_data: TaskCreate,
                 db: Session = Depends(get_db)):
    return task_service.create(task_data, db)

@router.put("/update/{id}", response_model=TaskResponse)
async def update(id: UUID,
                 task_data: TaskUpdate,
                 db: Session = Depends(get_db)):
    return task_service.update(id, task_data, db)

@router.delete("/delete/{id}")
async def delete(id: UUID, db: Session = Depends(get_db)):
    task_service.delete(id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/update-status/{id}", response_model=TaskResponse)
async def update_status(id: UUID, db: Session = Depends(get_db)):
    return task_service.update_status(id, db)

@router.get("/all", response_model=list[TaskResponse])
async def get_all(db: Session = Depends(get_db)):
    return task_service.get_all(db)