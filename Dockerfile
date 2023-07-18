FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir service
WORKDIR /service

RUN apk update && apk add postgresql-dev gcc musl-dev python3-dev libffi-dev openssl-dev 

RUN pip install --upgrade pip

COPY poetry.toml pyproject.toml poetry.lock /service/

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry config installer.max-workers 10 \
    && poetry install --no-dev --no-root --no-interaction --no-ansi -vvv

COPY . /service/

CMD ["poetry", "run", "python", "-m", "app"]

EXPOSE 8000