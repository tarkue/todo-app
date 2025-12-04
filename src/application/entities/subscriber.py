from asyncio import Queue, sleep
from uuid import UUID, uuid4

from src.domain.entities.event import Event
from src.domain.entities.task import Task


class TaskSubscriber:
    def __init__(self) -> None:
        self.id = uuid4()
        self.__queue = Queue[Event[Task]]()

    async def receive_event(self, event: Event[Task]):
        await self.__queue.put(event)

    def __eq__(self, value):
        if isinstance(value, UUID):
            return self.id == value
        return self.id == self.id

    async def __iter__(self):
        while True:
            if self.__queue.empty():
                await sleep(1)
            else:
                event = await self.__queue.get()
                yield event
