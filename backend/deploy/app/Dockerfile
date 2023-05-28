FROM python:3.11

ENV PYTHONBUFFERED=1 POETRY_VERSION=1.3.1 PORT=8000

RUN pip install poetry==$POETRY_VERSION && poetry config virtualenvs.create false

WORKDIR /app

COPY backend/poetry.lock backend/pyproject.toml ./


RUN poetry install --only main --no-root

COPY /backend .

RUN python manage.py collectstatic --noinput

EXPOSE $PORT

#RUN docker run -p 6378:6379 -d redis:5

CMD python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000