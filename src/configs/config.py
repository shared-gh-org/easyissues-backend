from fastapi import FastAPI
from src.configs.app_settings import AppSettings


def get_app_settings() -> AppSettings:
    return AppSettings()


def add_middleware(app: FastAPI) -> None:
    """Function to implement middleware.

    Not implemented yet.
    """
    pass
