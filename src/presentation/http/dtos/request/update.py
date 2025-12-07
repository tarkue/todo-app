from typing import Optional

from pydantic import BaseModel, Field

from src.domain.enums.task_status import TaskStatus


class UpdateTaskRequestDTO(BaseModel):
    title: Optional[str] = Field(default=None, examples=["Заголовок задачи"], max_length=120, min_length=1)
    description: Optional[str] = Field(default=None, examples=["Необязательное поле - это описание задачи"], max_length=500)
    status: Optional[TaskStatus] = Field(default=None)