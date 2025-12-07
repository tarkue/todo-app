from typing import AsyncIterable

from httpx import AsyncClient

from src.domain.entities.task import CreateTask
from src.domain.ports.external import ExternalServicePort
from src.domain.repositories.task import TaskRepository
from src.infrastructure.config import env


class ExternalService(ExternalServicePort):
    def __init__(self, task_repository: TaskRepository) -> None:
        self.__task_repository = task_repository

    async def get_external_tasks(self) -> AsyncIterable[TaskRepository]:
        async with AsyncClient(base_url=env.external.url) as client:
            response = await client.get("")
            external_task_list = response.json()
            
            if response.status_code == 200:
                create_task_list = [
                    CreateTask(
                        title=task["title"], 
                        description=task["description"]
                    ) for task in external_task_list
                ]
                await self.__task_repository.create_many(create_task_list)
                    
            