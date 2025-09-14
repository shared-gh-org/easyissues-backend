from src.configs.config import get_app_settings
from src.configs.config import add_middleware
from contextlib import asynccontextmanager
from src.api import health_controller
from src.api.v1 import repo_controller
from fastapi import FastAPI

from src.dependency.database import sessionmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    if sessionmanager._engine is not None:
        await sessionmanager.close()


def get_app() -> FastAPI:
    """Instanciating and setting up FastAPI application."""
    settings = get_app_settings()

    app = FastAPI(**settings.fastapi_kwargs, lifespan=lifespan)

    add_middleware(app)

    app.include_router(health_controller.router)
    app.include_router(repo_controller.router)

    return app


app = get_app()
