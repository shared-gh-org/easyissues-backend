from fastapi import APIRouter
from src.services.impl.health_service import HealthService


router = APIRouter(prefix="/api/health", tags=["health"])
health_service = HealthService()


@router.get("")
async def health_check():
    return await health_service.health_check()
