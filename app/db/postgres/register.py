from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.config import settings


TORTOISE_ORM = {
    "connections": {"default": str(settings.db_uri)},
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=settings.db_uri,
        modules={"models": ["app.db.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    