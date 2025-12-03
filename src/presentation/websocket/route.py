from typing import List

from fastapi import APIRouter, WebSocket

websocket_router = APIRouter(
    prefix="/ws",
    tags=["WebSocket"],
)


@websocket_router.websocket("/tasks")
async def update(
    websocket: WebSocket,
) -> None:
    ...