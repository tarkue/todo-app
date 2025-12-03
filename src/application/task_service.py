from typing import Iterable
from uuid import UUID, uuid4

from fastapi import BackgroundTasks

from src.application.external_service import ExternalService
from src.domain.entities.task import Task
from src.domain.ports.external import ExternalServicePort
from src.domain.ports.task import TaskServicePort
from src.domain.repositories.task import TaskRepository


class TaskService(TaskServicePort):
    def __init__(
        self, 
        task_repository: TaskRepository, 
        external_service: ExternalServicePort = None,
        background_tasks: BackgroundTasks = None,
    ) -> None:
        self.__repository = task_repository
        self.__background_tasks = background_tasks
        self.__external = external_service
        

    async def generate(self) -> Task: 
        async def background_task():
            tasks = await self.__external.get_external_tasks()
            await self.__repository.create_many(tasks)

        self.__background_tasks.add_task(background_task)


    async def get_all(self) -> Iterable[Task]: 
        return await self.__repository.get_all(id)


    async def get_by_id(self, id: UUID) -> Task: 
        return await self.__repository.get_by_id(id)


    async def update(self, data: Task) -> Task: 
        return await self.__repository.update(id)


    async def create(self, data: Task) -> Task: 
        data.id = uuid4()
        return await self.__repository.create(data.id)


    async def delete(self, id: UUID) -> Task:
        return await self.__repository.delete(id)
