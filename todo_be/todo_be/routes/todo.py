from typing import Optional
from uuid import UUID
from fastapi import APIRouter

from todo_be.core.logger import get_logger
from todo_be.models.dto.todo import (
    CreateTodoDTOin,
    GetTodoDTOout,
    ListTodoDTOout,
    UpdateTodoDTOin,
)
from todo_be.services.todo import TodoService


class TodoRouter:
    @staticmethod
    def get_router(service: TodoService):
        logger = get_logger()
        logger.debug('Creating todo router')
        todo_router = APIRouter(prefix='/todos', tags=['todos'])

        @todo_router.get(
            '', response_model=ListTodoDTOout, response_model_exclude_none=True
        )
        def list() -> ListTodoDTOout:
            return service.list()

        @todo_router.get(
            '/{uuid}',
            response_model=GetTodoDTOout,
            response_model_exclude_none=True,
        )
        def get_by_uuid(uuid: UUID) -> Optional[GetTodoDTOout]:
            return service.get_by_uuid(uuid)

        @todo_router.post(
            '', response_model=GetTodoDTOout, response_model_exclude_none=True
        )
        def create(todo: CreateTodoDTOin) -> Optional[GetTodoDTOout]:
            return service.create(todo)

        @todo_router.put(
            '',
            response_model=GetTodoDTOout,
            response_model_exclude_none=True,
        )
        def update(todo: UpdateTodoDTOin) -> Optional[GetTodoDTOout]:
            return service.update(todo)

        @todo_router.delete('/{uuid}')
        def delete(uuid: UUID) -> Optional[GetTodoDTOout]:
            return service.delete(uuid)

        @todo_router.put('/{uuid}/complete')
        def complete(uuid: UUID) -> Optional[GetTodoDTOout]:
            return service.complete(uuid)

        return todo_router
