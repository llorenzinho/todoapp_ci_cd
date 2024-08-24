from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from todo_be.core.config.db_config import DBConfig
from todo_be.core.config.log_config import LogConfig
from todo_be.core.constants import base_dir


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=f'{base_dir}/application.conf')
    http_interface: str = '0.0.0.0'
    http_port: int = 8000
    log_config: LogConfig = LogConfig()
    db_config: DBConfig = DBConfig()


@lru_cache
def get_config():
    return AppConfig()
