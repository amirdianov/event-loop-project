FROM python:3.11

ENV PYTHONBUFFERED=1 POETRY_VERSION=1.3.1 PORT=8000

RUN pip install poetry==$POETRY_VERSION && poetry config virtualenvs.create false

WORKDIR /app/backend

COPY backend/poetry.lock backend/pyproject.toml ./


RUN poetry install --only main --no-root

COPY /backend .

RUN python manage.py collectstatic --noinput

EXPOSE $PORT

CMD sh -c 'sleep 10 && celery -A eventloop worker -l info & celery -A eventloop beat -l info & python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT'
