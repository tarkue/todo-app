from fastapi import APIRouter, BackgroundTasks, Depends
from typing_extensions import Annotated

from src.application.external_service import ExternalService
from src.application.task_service import TaskService
from src.infrastructure.task.task_repository import SQLTaskRepository

router = APIRouter(
    prefix="/task-generator",
    tags=["task-generator"],
)

def get_task_service(
    task_repository: Annotated[SQLTaskRepository, Depends()],
    external_service: Annotated[ExternalService, Depends()],
    background_tasks: BackgroundTasks,
) -> TaskService:
    return TaskService(
        task_repository=task_repository,
        external_service=external_service,
        background_tasks=background_tasks,
    )

@router.post("/run")
async def run(
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    return await task_service.generate()