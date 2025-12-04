from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from src.domain.enums.task_status import TaskStatus


@dataclass
class Task:
  """
  Объект Задачи

  Напоминание о том, что необходимо сделать.
  """
  id: UUID
  title: str
  description: Optional[str]
  status: TaskStatus = TaskStatus.IN_PROGRESS