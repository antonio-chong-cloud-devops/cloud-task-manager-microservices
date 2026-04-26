from fastapi import APIRouter
from app.models.task import Task
from app.services.task_service import get_all_tasks, create_task

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return get_all_tasks()

@router.post("/tasks")
def create_new_task(task: Task):
    return create_task(task)