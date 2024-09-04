from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from todo_be.core.config.config import get_config
from todo_be.core.logger import get_logger
from todo_be.db.dao.todo_dao import TodoDao
from todo_be.db.database import Database
from todo_be.routes.healthcheck import HealthCheckRouter
from todo_be.routes.todo import TodoRouter
from todo_be.routes.version import VersionRouter
from todo_be.services.todo import TodoService

logger = get_logger()
database = Database(get_config().db_config)

todo_dao = TodoDao(database)

todo_service = TodoService(todo_dao)


@asynccontextmanager
async def lifespan(fastapi: FastAPI):
    logger.info('Starting service ...')
    database.connect()
    database.init_mappings()
    logger.info('Service started')
    yield
    logger.info('Stopping service ...')


app = FastAPI(title='TODO BE', lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    allow_headers=[
        'access-control-allow-origin',
        'content-type',
    ],
)

app.include_router(HealthCheckRouter.get_router())
app.include_router(VersionRouter.get_router())
app.include_router(TodoRouter.get_router(todo_service))
