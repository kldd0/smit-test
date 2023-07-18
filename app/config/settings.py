import pydantic as pd
import pydantic_settings as pd_s
from dataclasses import dataclass


class MainSettings(pd_s.BaseSettings):
    postgres_dialect_driver: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_db: str

    @property
    def db_uri(self):
        return pd.PostgresDsn.build(
            scheme=self.postgres_dialect_driver,
            username=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            path=self.postgres_db
        )

    class Config:
        env_file = ".env"


settings = MainSettings()