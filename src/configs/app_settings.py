import os
from typing import Any, Dict

from pydantic import PostgresDsn
from dotenv import load_dotenv

load_dotenv(".env")


class AppSettings:
    """Bundle all app settings."""

    # FastAPI App settings
    docs_url: str = "/docs"
    title: str = os.getenv("APP_TITLE")
    version: str = os.getenv("APP_VERSION")
    description: str = os.getenv("APP_DESCRIPTION")

    # database settings
    postgres_driver: str = "asyncpg"
    postgres_user: str = os.getenv("POSTGRES_USER")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD")
    postgres_server: str = os.getenv("POSTGRES_SERVER")
    postgres_port: int = os.getenv("POSTGRES_PORT")
    postgres_db: str = os.getenv("POSTGRES_DB")

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "docs_url": self.docs_url,
            "title": self.title,
            "version": self.version,
            "description": self.description,
        }

    @property
    def database_settings(self) -> Dict[str, Any]:
        return {
            "postgres_user": self.postgres_user,
            "postgres_password": self.postgres_password,
            "postgres_server": self.postgres_server,
            "postgres_port": self.postgres_port,
            "postgres_db": self.postgres_db,
        }

    @property
    def database_url(self) -> PostgresDsn:
        """Create a valid Postgres database url."""
        return f"postgresql+{self.postgres_driver}://{self.postgres_user}:" + \
            f"{self.postgres_password}@{self.postgres_server}" + \
            f":{self.postgres_port}/{self.postgres_db}"
