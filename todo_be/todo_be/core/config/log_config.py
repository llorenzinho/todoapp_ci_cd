from typing import Dict
from pydantic_settings import BaseSettings, SettingsConfigDict
from logging import Filter

from todo_be.core.constants import base_dir


class HealthCheckFilter(Filter):
    def filter(self, record):
        return record.getMessage().find('/healtz') == -1


class LogConfig(BaseSettings):
    """Logging configuration to be set for the server"""

    model_config = SettingsConfigDict(env_file=f'{base_dir}/logger.conf')
    logger_name: str = 'radicalbit-ai-monitoring'
    log_format: str = '%(levelname)s | %(asctime)s | %(message)s'
    log_level: str = 'INFO'

    # logger dictConfig
    version: int = 1
    disable_existing_loggers: bool = False

    formatters: Dict = {
        'default': {
            'format': log_format,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'access': {
            'format': log_format,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    }

    filters: Dict = {
        'healthcheck_filter': {'()': HealthCheckFilter},
    }
    handlers: Dict = {
        'default': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        },
        'access': {
            'formatter': 'access',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'filters': ['healthcheck_filter'],
        },
    }
    loggers: Dict = {
        logger_name: {
            'handlers': ['default'],
            'level': log_level.upper(),
            'propagate': False,
        },
        'uvicorn.error': {
            'handlers': ['default'],
            'level': log_level.upper(),
            'propagate': False,
        },
        'uvicorn.access': {
            'handlers': ['access'],
            'level': log_level.upper(),
            'propagate': False,
        },
        'root': {
            'handlers': ['default'],
            'level': log_level.upper(),
            'propagate': False,
        },
    }
