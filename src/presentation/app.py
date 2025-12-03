from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infrastructure.config import env
from src.presentation.http.router import http_router
from src.presentation.websocket.route import websocket_router

app = FastAPI(
    title=env.app.title,
    description=env.app.description,
    version=env.app.version,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=1728000
)  


app.include_router(http_router)
app.include_router(websocket_router)