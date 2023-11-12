FROM python:3.11

ENV PYTHONBUFFERED=1 POETRY_VERSION=1.3.1 PORT=8000

RUN pip install poetry==$POETRY_VERSION && poetry config virtualenvs.create false

WORKDIR /app/backend

COPY backend/poetry.lock backend/pyproject.toml ./

RUN poetry install --only main --no-root

COPY /backend .

EXPOSE $PORT

COPY deploy/app/back/entrypoint.sh /app/scripts/
RUN chmod +x -R /app/scripts/
ENTRYPOINT ["/app/scripts/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

