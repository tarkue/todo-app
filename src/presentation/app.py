from fastapi import FastAPI

from src.presentation.http.router import http_router
from src.presentation.websocket.route import websocket_router

app = FastAPI()

app.add_api_route(http_router)
app.add_api_websocket_route(websocket_router)