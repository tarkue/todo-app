from dataclasses import dataclass
from typing import Optional
from uuid import UUID, uuid4

from src.domain.enums.task_status import TaskStatus


@dataclass
class Task:
  """
  Объект Задачи

  Напоминание о том, что необходимо сделать.
  """
  title: str
  id: Optional[UUID]
  description: Optional[str]
  status: TaskStatus = TaskStatus.IN_PROGRESS


@dataclass
class CreateTask:
  """
  Объект Задачи

  Напоминание о том, что необходимо сделать.
  """
  title: str
  description: Optional[str]