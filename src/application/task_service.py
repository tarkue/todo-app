from asyncio import Task
from typing import Iterable
from uuid import UUID

from src.domain.ports.task import TaskServicePort
from src.domain.repositories.task import TaskRepository


class TaskService(TaskServicePort):

    def __init__(self, task_repository: TaskRepository) -> None:
        self.__repository = task_repository
        

    async def generate(self) -> Task: ...

    async def get_all(self) -> Iterable[Task]: ...

    async def get_by_id(self, id: UUID) -> Task: ...

    async def update(self, object: Task) -> Task: ...


    async def delete(self, id: UUID) -> Task: ...