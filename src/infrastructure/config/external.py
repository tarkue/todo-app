
from _default import CONFIG_DEFAULT
from pydantic_settings import BaseSettings, SettingsConfigDict


class External(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='EXTERNAL_', **CONFIG_DEFAULT)

    url: str