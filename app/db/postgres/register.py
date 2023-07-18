from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.config import settings


DB_MODELS = ["app.db.postgres.models"]
TORTOISE_ORM_CONFIG = {
    "connections": {
        "default": {
            "engine": 'tortoise.backends.asyncpg',
            "credentials": {
                "host": settings.postgres_host,
                "port": settings.postgres_port,
                "user": settings.postgres_user,
                "password": settings.postgres_password,
                "database": settings.postgres_db,
            }
        },
    },
    "apps": {
        "models": {
            "models": DB_MODELS,
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM_CONFIG,
        generate_schemas=True,
        add_exception_handlers=True,
    )