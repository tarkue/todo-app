import abc
from typing import AsyncIterable

from src.domain.repositories.task import TaskRepository


class ExternalServicePort(abc.ABC):
    """
    Сервис, который получает данные со стороннего сайта
    """
    @abc.abstractmethod
    async def get_external_tasks() -> AsyncIterable[TaskRepository]: ...