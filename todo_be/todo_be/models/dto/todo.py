from typing import List, Self
from uuid import UUID
from datetime import datetime

from todo_be.db.tables.todo import Todo
from todo_be.models.dto.base import BaseDTO


class CreateTodoDTOin(BaseDTO):
    title: str
    description: str
    completed: bool = False


class GetTodoDTOout(BaseDTO):
    uuid: UUID
    title: str
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime


class ListTodoDTOout(BaseDTO):
    todos: List[GetTodoDTOout]

    @staticmethod
    def from_models(models: List[Todo]) -> Self:
        return ListTodoDTOout(
            todos=[GetTodoDTOout.model_validate(model) for model in models]
        )


class UpdateTodoDTOin(BaseDTO):
    uuid: UUID
    title: str
    description: str
    completed: bool


class CompleteDTOin(BaseDTO):
    uuid: UUID
    completed: bool
