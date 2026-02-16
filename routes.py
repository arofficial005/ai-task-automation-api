from fastapi import APIRouter, BackgroundTasks
from app.services import process_task

router = APIRouter(prefix="/tasks")

@router.post("/run")
def run_task(task_name: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_task, task_name)
    return {"message": f"Task '{task_name}' started"}
