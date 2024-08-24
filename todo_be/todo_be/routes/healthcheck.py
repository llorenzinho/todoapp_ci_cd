from http import HTTPStatus
from fastapi import APIRouter

from todo_be.core.logger import get_logger
from todo_be.models.dto.healthz import HealtcheckOutDTO


class HealthCheckRouter:
    @staticmethod
    def get_router():
        logger = get_logger()
        logger.debug('Creating health check router')
        health_check_router = APIRouter()

        @health_check_router.get(
            '/healtz', response_model=HealtcheckOutDTO, status_code=HTTPStatus.OK
        )
        def health_check():
            return HealthCheckRouter.health_check()

        return health_check_router

    @staticmethod
    def health_check():
        return HealtcheckOutDTO(status=HTTPStatus.OK, message='OK')
