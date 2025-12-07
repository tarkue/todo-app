from typing import List, Union

from src.application.entities.subscriber import TaskSubscriber
from src.domain.entities.event import Event
from src.domain.entities.task import Task
from src.domain.helpers.singleton_meta import SingletonABCMeta
from src.domain.ports.real_time import RealTimeServicePort


class RealTimeTaskService(RealTimeServicePort[Union[Task, List[Task]]], metaclass=SingletonABCMeta):
    def __init__(self) -> None:
        self.__subscribers: List[TaskSubscriber] = []


    async def publish(self, event: Event[Task]) -> None:
        for subscriber in self.__subscribers:
            await subscriber.receive_event(event)

    def subscribe(self):
        subscriber = TaskSubscriber()
        self.__subscribers.append(subscriber)
        return subscriber

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)
