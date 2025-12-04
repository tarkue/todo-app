from fastapi import APIRouter, Depends, WebSocket
from fastapi.encoders import jsonable_encoder
from typing_extensions import Annotated, List

from src.application.services.task import TaskService
from src.presentation.depends.task_service import get_task_service

websocket_router = APIRouter(
    prefix="/ws",
    tags=["WebSocket"],
)

@websocket_router.websocket("/tasks")
async def update(
    websocket: WebSocket,
    task_service: Annotated[TaskService, Depends(get_task_service)]
) -> None:
    async def handle(message):
        websocket.send_json(
            jsonable_encoder(
                message.model_dump()    
            )
        )

    task_service.subscribe(handle)

    