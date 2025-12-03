import abc
from typing import AsyncIterator, Generic, TypeVar

from src.domain.entities.event import Event

T = TypeVar("T")

class RealTimeServicePort(abc.ABC, Generic[T]):
    @abc.abstractmethod
    async def subscribe(self) -> AsyncIterator[Event[T]]: ...

    @abc.abstractmethod
    async def emit(self, event: Event[T]) -> Event[T]: ...
