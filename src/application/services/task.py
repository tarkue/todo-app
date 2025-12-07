from typing import Awaitable, Callable, Iterable
from uuid import UUID, uuid4

from fastapi import BackgroundTasks

from src.domain.entities.event import Event
from src.domain.entities.task import CreateTask, Task
from src.domain.enums.event_type import EventType
from src.domain.ports.external import ExternalServicePort
from src.domain.ports.real_time import RealTimeServicePort
from src.domain.ports.task import TaskServicePort
from src.domain.repositories.task import TaskRepository


class TaskService(TaskServicePort):
    def __init__(
        self, 
        task_repository: TaskRepository, 
        external_service: ExternalServicePort = None,
        background_tasks: BackgroundTasks = None,
        real_time_service: RealTimeServicePort[Task] = None
    ) -> None:
        self.__repository = task_repository
        self.__background_tasks = background_tasks
        self.__external = external_service
        self.__real_time_service = real_time_service
        

    async def subscribe(self, handle: Callable[[Event[Task]], Awaitable[None]]):
        subscriber = self.__real_time_service.subscribe()
        
        async for message in subscriber:
            try:
                await handle(message)
            except Exception:
                break

        self.__real_time_service.unsubscribe(subscriber)


    async def generate(self) -> Task: 
        async def background_task():
            tasks = await self.__external.get_external_tasks()
            result = await self.__repository.create_many(tasks)

            if self.__real_time_service:
                await self.__real_time_service.publish(Event(EventType.CREATE_MANY, result))

        self.__background_tasks.add_task(background_task)


    async def get_all(self) -> Iterable[Task]: 
        return await self.__repository.get_all()


    async def get_by_id(self, id: UUID) -> Task: 
        return await self.__repository.get_by_id(id)


    async def update(self, id: UUID, data: dict) -> Task: 
        current_task = await self.__repository.get_by_id(id)
        
        updated_task = Task(
            id=current_task.id,
            title=data.get("title", current_task.title),
            description=data.get("description", current_task.description),
            status=data.get("status", current_task.status)
        )
        
        result = await self.__repository.update(id, updated_task)
        if self.__real_time_service:
            await self.__real_time_service.publish(Event(EventType.UPDATE, result))
        return result


    async def create(self, data: CreateTask) -> Task: 
        result = await self.__repository.create(data)
        if self.__real_time_service:
            await self.__real_time_service.publish(Event(EventType.CREATE, result))
        return result


    async def delete(self, id: UUID) -> Task:
        result = await self.__repository.delete(id)
        if self.__real_time_service:
            await self.__real_time_service.publish(Event(EventType.DELETE, result))
        return result 
