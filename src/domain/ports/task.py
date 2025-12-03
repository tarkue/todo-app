import abc
from typing import Iterable
from uuid import UUID

from src.domain.entities.task import Task


class TaskServicePort(abc.ABC):
    @abc.abstractmethod
    async def generate(self) -> Task: ...

    @abc.abstractmethod
    async def get_all(self) -> Iterable[Task]: ...

    @abc.abstractmethod
    async def get_by_id(self, id: UUID) -> Task: ...

    @abc.abstractmethod
    async def update(self, object: Task) -> Task: ...

    @abc.abstractmethod
    async def delete(self, id: UUID) -> Task: ...