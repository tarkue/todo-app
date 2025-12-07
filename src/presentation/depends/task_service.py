from fastapi import BackgroundTasks, Depends
from typing_extensions import Annotated

from src.application.services.external import ExternalService
from src.application.services.real_time import RealTimeTaskService
from src.application.services.task import TaskService
from src.infrastructure.task.task_repository import SQLTaskRepository


def get_task_repository() -> SQLTaskRepository:
    return SQLTaskRepository()


def get_external_service() -> ExternalService:
    return ExternalService()


def get_real_time_service() -> RealTimeTaskService:
    return RealTimeTaskService()


def get_task_service(
    task_repository: Annotated[SQLTaskRepository, Depends(get_task_repository)],
    external_service: Annotated[ExternalService, Depends(get_external_service)],
    background_tasks: BackgroundTasks,
    real_time_service: Annotated[RealTimeTaskService, Depends(get_real_time_service)]
): 
    return TaskService(
        task_repository=task_repository,
        external_service=external_service,
        background_tasks=background_tasks,
        real_time_service=real_time_service,
    )
