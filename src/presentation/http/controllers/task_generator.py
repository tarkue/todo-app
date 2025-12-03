from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from domain.services.task import TaskService

router = APIRouter(
    prefix="/task-generator",
    tags=["task-generator"],
)

@router.post("/run")
def run(task_service: Annotated[TaskService, Depends]):
    return task_service.generate()