from typing import Iterable, List
from uuid import UUID

from fastapi import HTTPException, status

from src.domain.entities.task import CreateTask, Task
from src.domain.helpers.singleton_meta import SingletonABCMeta
from src.domain.repositories.task import TaskRepository
from src.infrastructure.database import db
from src.infrastructure.database.models.task import TaskModel


class SQLTaskRepository(TaskRepository, metaclass=SingletonABCMeta): 
    async def get_all(self) -> Iterable[Task]: 
        models = await TaskModel.get_all()
        return [
            Task(
                id=model.id,
                title=model.title,
                description=model.description,
                status=model.status
            ) for model in models
        ]


    async def get_by_id(self, id: UUID) -> Task: 
        if not await TaskModel.exist_by_id(id):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Task not found."
            )

        return await TaskModel.find_by_id(id)


    async def update(self, id: UUID, data: Task) -> Task: 
        if not await TaskModel.exist_by_id(id):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Task not found."
            )

        values = {}
        if data.title is not None:
            values["title"] = data.title
        if data.description is not None:
            values["description"] = data.description
        if data.status is not None:
            values["status"] = data.status

        await TaskModel.update(id, values)
        return await TaskModel.find_by_id(id)


    async def create(self, data: CreateTask) -> Task: 
        return await TaskModel.create(title=data.title, description=data.description)


    async def create_many(self, objects: List[CreateTask]):
        tasks = [
            TaskModel(
                title=data.title,
                description=data.description,
            ) for data in objects
        ]
        
        db.add_all(tasks)
        await db.commit_rollback()

        return tasks


    async def delete(self, id: UUID) -> Task: 
        task = await TaskModel.find_by_id(id)
        if task is None:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Task not found."
            )
        await TaskModel.delete(id)
        return task
