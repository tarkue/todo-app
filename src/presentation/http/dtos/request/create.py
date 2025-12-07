from typing import Optional

from pydantic import BaseModel, Field


class CreateTaskRequestDTO(BaseModel):
    title: str = Field(examples=["Заголовок задачи"], max_length=120, min_length=1)
    description: Optional[str] = Field(default=None, examples=["Необязательное поле - это описание задачи"], max_length=500)
    