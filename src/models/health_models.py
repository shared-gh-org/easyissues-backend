from pydantic import BaseModel
from src.utils.constants import STATUSDOWN


class DatabasePublic(BaseModel):
    status: str = STATUSDOWN
    disk: str = "NaN"
    sessions: int = -1


class InternetPublic(BaseModel):
    status: str = STATUSDOWN
    latency: str = "NaN"
    throughput: str = "NaN"


class HealthPublic(BaseModel):
    internet: InternetPublic
    database: DatabasePublic
