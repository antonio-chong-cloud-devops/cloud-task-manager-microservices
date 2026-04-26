from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str

tasks = [
        {"id": 1, "title": "Primera tarea"},
        {"id": 2, "title": "Segunda tarea"}
    ]

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task.dict())
    return {
        "message": "Task created",
        "task": task
    }