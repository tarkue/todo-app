from dataclasses import dataclass

from .app import App
from .database import Database
from .external import External


@dataclass
class EnvironmentConfig:
    app: App = App()
    database: Database = Database()
    external: External = External()


env = EnvironmentConfig()