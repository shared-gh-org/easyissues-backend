from fastapi import APIRouter
from src.services.impl.repo_service import RepoService


router = APIRouter(prefix="/api/v1/repos", tags=["repositories"])

repo_service = RepoService()


@router.get("")
async def get_all():
    return await repo_service.get_all()
