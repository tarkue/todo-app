from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from src.application.services.task import TaskService
from src.presentation.depends.task_service import get_task_service

router = APIRouter(
    prefix="/task-generator",
    tags=["task-generator"],
)

@router.post("/run")
async def run(
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    return await task_service.generate()