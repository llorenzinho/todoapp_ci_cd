from typing import Optional
from uuid import uuid4, UUID
from datetime import datetime, UTC
from todo_be.core.logger import get_logger
from todo_be.db.dao.todo_dao import TodoDao
from todo_be.db.tables.todo import Todo
from todo_be.models.dto.todo import (
    CreateTodoDTOin,
    GetTodoDTOout,
    ListTodoDTOout,
    UpdateTodoDTOin,
)


class TodoService:
    def __init__(self, dao: TodoDao) -> None:
        self.dao = dao
        self.log = get_logger()

    def get_by_uuid(self, uuid: UUID) -> Optional[GetTodoDTOout]:
        self.log.debug(f'Get todo by uuid: {uuid}')
        return self.dao.get_by_uuid(uuid)

    def create(self, todo: CreateTodoDTOin) -> Optional[GetTodoDTOout]:
        self.log.debug(f'Create todo: {todo}')
        _todo = Todo(
            uuid=uuid4(),
            title=todo.title,
            description=todo.description,
            completed=False,
            created_at=datetime.now(tz=UTC),
            updated_at=datetime.now(tz=UTC),
        )
        return GetTodoDTOout.model_validate(self.dao.create(_todo))

    def update(self, todo: UpdateTodoDTOin) -> Optional[GetTodoDTOout]:
        self.log.debug(f'Update todo: {todo}')
        updated_todo = self.dao.update(todo.uuid, todo.model_dump())
        return GetTodoDTOout.model_validate(updated_todo)

    def delete(self, uuid: UUID) -> Optional[GetTodoDTOout]:
        self.log.debug(f'Delete todo: {uuid}')
        return GetTodoDTOout.model_validate(self.dao.delete(uuid))

    def list(self) -> ListTodoDTOout:
        self.log.debug('List todos')
        return ListTodoDTOout.from_models(self.dao.list())

    def complete(self, uuid: UUID) -> Optional[GetTodoDTOout]:
        self.log.debug(f'Complete todo: {uuid}')
        return self.dao.complete(uuid)
