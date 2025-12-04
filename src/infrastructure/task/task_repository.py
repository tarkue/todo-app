from typing import Iterable
from uuid import UUID

from fastapi import HTTPException, status

from src.domain.entities.task import Task
from src.domain.repositories.task import TaskRepository
from src.infrastructure.database.models.task import TaskModel


class SQLTaskRepository(TaskRepository): 
    async def get_all(self) -> Iterable[Task]: 
        return await TaskModel.get_all()

    async def get_by_id(self, id: UUID) -> Task: 
        if not await TaskModel.exist_by_id(id):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Message not found."
            )

        return await TaskModel.find_by_id(id)

    async def update(self, id: UUID, data: Task) -> Task: 
        if not await TaskModel.exist_by_id(id):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Message not found."
            )

        values = {}

        if data.title is not None:
            values["title"] = data.title

        if data.description is not None:
            values["description"] = data.description

        if data.status is not None:
            values["status"] = data.status

        return await TaskModel.update(id)

    async def create(self, data: Task) -> Task: 
        values = {
            "title": data.title,
            "description": data.description,
        }

        return await TaskModel.create(values)

    async def delete(self, id: UUID) -> Task: 
        return await TaskModel.delete(id)
