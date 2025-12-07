from apscheduler.schedulers.background import BackgroundScheduler
from httpx import Client
from uvicorn import run

from src.infrastructure.config import env
from src.presentation.app import app


def background_task():
    client = Client(base_url=env.background_task.url)
    client.post("/task-generator/run")

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(background_task, "interval", minutes =env.background_task.interval_in_minutes)
    scheduler.start()
    run(
        app, 
        host=env.app.host, 
        port=env.app.port
    )