from src.api import health_controller
from fastapi import FastAPI


app = FastAPI(title="Easy Issues")

app.include_router(health_controller.router)
