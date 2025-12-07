import abc
from typing import Iterable
from uuid import UUID

from src.domain.entities.task import CreateTask, Task


class TaskServicePort(abc.ABC):
    @abc.abstractmethod
    async def subscribe(self): ...
    
    @abc.abstractmethod
    async def generate(self) -> Task: ...

    @abc.abstractmethod
    async def get_all(self) -> Iterable[Task]: ...

    @abc.abstractmethod
    async def get_by_id(self, id: UUID) -> Task: ...

    @abc.abstractmethod
    async def create(self, object: CreateTask) -> Task: ...

    @abc.abstractmethod
    async def update(self, id: UUID, object: Task) -> Task: ...

    @abc.abstractmethod
    async def delete(self, id: UUID) -> Task: ...