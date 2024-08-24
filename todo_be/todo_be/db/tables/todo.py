from uuid import uuid4
from sqlalchemy import Boolean, Column, DateTime, Integer, String, UUID
from todo_be.db.database import BaseTable


class Todo(BaseTable):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(
        'UUID',
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        default=uuid4,
        primary_key=True,
    )
    title = Column('TITLE', String, nullable=False)
    description = Column('DESCRIPTION', String, nullable=False)
    completed = Column('COMPLETED', Boolean, nullable=False)
    created_at = Column('CREATED_AT', DateTime, nullable=False)
    updated_at = Column('UPDATED_AT', DateTime, nullable=False)
