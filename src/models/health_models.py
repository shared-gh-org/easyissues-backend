from pydantic import BaseModel


class HealthPublic(BaseModel):
    status: str
