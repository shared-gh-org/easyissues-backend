from fastapi import APIRouter
from src.services.impl.health_service import HealthService


router = APIRouter(prefix="/api/health", tags=["health"])
health_service = HealthService()


@router.get("")
def health_check():
    return health_service.health_check()
