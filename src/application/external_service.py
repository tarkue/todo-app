from typing import Iterable

from src.domain.ports.external import ExternalServicePort
from src.domain.repositories.task import TaskRepository


class ExternalService(ExternalServicePort): 
    async def get_external_tasks() -> Iterable[TaskRepository]: ...