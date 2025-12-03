from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from src.application.task_service import TaskService
from src.infrastructure.task.task_repository import SQLTaskRepository

router = APIRouter(
    prefix="/task-generator",
    tags=["task-generator"],
)

@router.post("/run")
def run(task_service: Annotated[TaskService, Depends(SQLTaskRepository)]):
    return task_service.generate()