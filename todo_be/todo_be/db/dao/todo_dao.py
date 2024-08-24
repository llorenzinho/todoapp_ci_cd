from datetime import UTC, datetime
from typing import Optional
from uuid import UUID

import sqlalchemy
from todo_be.db.dao.base import BaseDao
from todo_be.db.tables.todo import Todo


class TodoDao(BaseDao):
    def get_by_uuid(self, uuid: UUID) -> Optional[Todo]:
        with self.database.begin_session() as session:
            return session.query(Todo).filter(Todo.uuid == uuid).one_or_none()

    def create(self, todo: Todo) -> Todo:
        with self.database.begin_session() as session:
            session.add(todo)
            session.flush()
            return todo

    def update(self, uuid: UUID, todo: dict) -> Optional[Todo]:
        with self.database.begin_session() as session:
            query = (
                sqlalchemy.update(Todo)
                .where(Todo.uuid == uuid)
                .values(**todo, updated_at=datetime.now(tz=UTC))
            )
            session.execute(query)
            return session.query(Todo).filter(Todo.uuid == uuid).one_or_none()

    def delete(self, uuid: UUID) -> Todo:
        with self.database.begin_session() as session:
            to_delete = session.query(Todo).filter(Todo.uuid == uuid).one_or_none()
            query = sqlalchemy.delete(Todo).where(Todo.uuid == uuid)
            session.execute(query)
            return to_delete

    def list(self) -> list[Todo]:
        with self.database.begin_session() as session:
            return session.query(Todo).all()

    def complete(self, uuid: UUID) -> Optional[Todo]:
        with self.database.begin_session() as session:
            query = (
                sqlalchemy.update(Todo)
                .where(Todo.uuid == uuid)
                .values(completed=True, updated_at=datetime.now(tz=UTC))
            )
            session.execute(query)
            return session.query(Todo).filter(Todo.uuid == uuid).one_or_none()
