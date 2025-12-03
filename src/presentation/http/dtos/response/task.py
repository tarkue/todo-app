from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from src.domain.enums.task_status import TaskStatus


class TaskResponseDTO(BaseModel): 
  id: UUID
  title: str 
  description: Optional[str]
  status: TaskStatus