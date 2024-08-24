FROM python:3.12.5-bookworm

WORKDIR /todo_be

COPY poetry.lock pyproject.toml ./
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev python3-dev && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    pip install --no-cache-dir poetry==1.8.3 && \
    poetry export --only migrations -f requirements.txt -o requirements.txt && \
    pip install --no-cache-dir -r requirements.txt

COPY ./alembic /todo_be/alembic
COPY alembic.ini /todo_be/alembic.ini
COPY ./todo_be /todo_be/todo_be

CMD ["alembic", "upgrade", "head"]