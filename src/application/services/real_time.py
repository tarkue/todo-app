from typing import List

from src.application.entities.subscriber import TaskSubscriber
from src.application.helpers.singleton_meta import SingletonMeta
from src.domain.entities.event import Event
from src.domain.entities.task import Task
from src.domain.ports.real_time import RealTimeServicePort


class RealTimeTaskService(SingletonMeta, RealTimeServicePort[Task]):
    def __init__(self) -> None:
        super().__init__()
        self.__subscribers: List[TaskSubscriber] = []


    async def publish(self, event: Event[Task]) -> None:
        for subscriber in self.__subscribers:
            subscriber.receive_event(event)

    def subscribe(self):
        subscriber = TaskSubscriber()
        self.__subscribers.append(subscriber)
        return subscriber

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)
