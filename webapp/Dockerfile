FROM python:3.12-alpine AS builder

WORKDIR /app

COPY requirements/dev.txt /app/requirements/dev.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements/dev.txt

COPY . /app

FROM builder AS dev

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
