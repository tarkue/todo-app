from _default import CONFIG_DEFAULT
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Database(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='DATABASE_', **CONFIG_DEFAULT)

    host: str
    port: str
    name: str
    user: str
    password: str

    @property
    def url(self):
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.name
        ) 