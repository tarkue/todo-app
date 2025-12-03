from typing import Optional

from pydantic import Field

from domain.enums.task_status import TaskStatus


class UpdateTaskRequestDTO:
    title: Optional[str] = Field(examples="Заголовок задачи", max_length=120, min_length=1)
    description: Optional[str] = Field(examples="Необязательное поле - это описание задачи", max_length=500)
    status: TaskStatus = Field(examples=TaskStatus.COMPLETED)