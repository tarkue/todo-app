from fastapi import BackgroundTasks, Depends
from typing_extensions import Annotated

from src.application.services.external import ExternalService
from src.application.services.real_time import RealTimeTaskService
from src.application.services.task import TaskService
from src.infrastructure.task.task_repository import SQLTaskRepository


def get_task_service(
    task_repository: Annotated[SQLTaskRepository, Depends()],
    external_service: Annotated[ExternalService, Depends()],
    background_tasks: BackgroundTasks,
): 
    return TaskService(
        task_repository=task_repository,
        external_service=external_service,
        background_tasks=background_tasks,
        real_time_service=RealTimeTaskService,
    )
