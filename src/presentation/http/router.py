
from fastapi import APIRouter

from .controllers.task import router as task_router
from .controllers.task_generator import router as task_gerator_router

http_router = APIRouter()

http_router.include_router(task_router)
http_router.include_router(task_gerator_router)
