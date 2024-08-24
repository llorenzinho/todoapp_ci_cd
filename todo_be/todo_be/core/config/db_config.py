from pydantic_settings import BaseSettings, SettingsConfigDict

from todo_be.core.constants import base_dir


class DBConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=f'{base_dir}/db.conf')

    db_host: str = 'localhost'
    db_port: int = 5432
    db_user: str = 'postgres'
    db_pwd: str = 'postgres'
    db_name: str = 'postgres'
    db_schema: str = 'public'
