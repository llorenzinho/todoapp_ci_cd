from todo_be.db.database import Database


class BaseDao:
    def __init__(self, database: Database) -> None:
        self.database = database
