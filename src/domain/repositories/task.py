import abc
from typing import Iterable, List
from uuid import UUID

from src.domain.entities.task import Task


class TaskRepository(abc.ABC):
    @abc.abstractmethod
    async def get_all(self) -> Iterable[Task]: ...

    @abc.abstractmethod
    async def get_by_id(self, id: UUID) -> Task: ...

    @abc.abstractmethod
    async def create(self, object: Task) -> Task: ...

    @abc.abstractmethod
    async def create_many(self, object: List[Task]) -> Task: ...

    @abc.abstractmethod
    async def update(self, id: UUID, object: Task) -> Task: ...

    @abc.abstractmethod
    async def delete(self, id: UUID) -> Task: ...