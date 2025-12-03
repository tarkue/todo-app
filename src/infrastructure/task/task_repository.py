from asyncio import Task
from typing import Iterable
from uuid import UUID

from src.domain.repositories.task import TaskRepository


class SQLTaskRepository(TaskRepository): 
    async def get_all(self) -> Iterable[Task]: 
        ...

    async def get_by_id(self, id: UUID) -> Task: ...

    async def update(self, data: Task) -> Task: ...

    async def create(self, data: Task) -> Task: ...

    async def delete(self, id: UUID) -> Task: ...