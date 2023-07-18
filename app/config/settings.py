import pydantic as pd
import pydantic_settings as pd_s
from dataclasses import dataclass


class MainSettings(pd_s.BaseSettings):
    postgres_dialect_driver: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_db: str
    postgres_port: int

    class Config:
        env_file = ".env"


settings = MainSettings()