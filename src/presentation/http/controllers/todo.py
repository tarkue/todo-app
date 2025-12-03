from typing import Iterable
from uuid import UUID

from fastapi import APIRouter, Depends, status
from typing_extensions import Annotated

from domain.entities.task import Task
from domain.services.task import TaskService
from presentation.http.dtos.create import CreateTaskRequestDTO
from presentation.http.dtos.update import UpdateTaskRequestDTO

router = APIRouter(
    prefix="/tasks",
    tags=["task-generator"],
)

@router.get("/", status_code=status.HTTP_200_OK, description="Возвращает список задач")
async def get_all(task_service: Annotated[TaskService, Depends]) -> Iterable[Task]:
    return await task_service.get_all()


@router.get("/{id}", status_code=status.HTTP_200_OK, description="Возвращает задачу по уникальному идентификатору")
async def get_by_id(id: UUID, task_service: Annotated[TaskService, Depends]) -> Task:
    return await task_service.get_by_id(id)


@router.post("/", status_code=status.HTTP_201_CREATED, description="Добавляет новую задачу")
async def create(dto: CreateTaskRequestDTO, task_service: Annotated[TaskService, Depends]) -> Task:
    return await task_service.create(dto)


@router.patch("/{id}", status_code=status.HTTP_200_OK, description="Частично обновляет задачу")
async def update(dto: UpdateTaskRequestDTO, task_service: Annotated[TaskService, Depends]) -> Task:
    return await task_service.update(dto)


@router.delete("/{id}", status_code=status.HTTP_200_OK, description="Удаляет задачу без возможности восстановления")
async def delete(id: UUID, task_service: Annotated[TaskService, Depends]) -> Task:
    return await task_service.delete(id)

  