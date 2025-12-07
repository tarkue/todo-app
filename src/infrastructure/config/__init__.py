from dataclasses import dataclass

from .app import App
from .background_task import BackgroundTask
from .database import Database
from .external import External


@dataclass
class EnvironmentConfig:
    app: App = App()
    database: Database = Database()
    external: External = External()
    background_task: BackgroundTask = BackgroundTask()


env = EnvironmentConfig()