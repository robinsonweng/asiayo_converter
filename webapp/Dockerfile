FROM python:3.12-alpine AS builder

ARG USER_NAME

RUN adduser -D ${USER_NAME}
USER ${USER_NAME}

RUN pip install --upgrade pip

WORKDIR /app

COPY --chown=${USER_NAME}:${USER_NAME} requirements/dev.txt requirements/dev.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements/dev.txt

ENV PATH="/home/${USER_NAME}/.local/bin:${PATH}"

COPY --chown=${USER_NAME}:${USER_NAME} . /app

FROM builder AS dev

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
