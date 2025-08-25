from src.repository.dao.repo_dao import RepoDao
from src.models.repo_models import RepoPublic


class RepoService:
    def __init__(self, repo_dao: RepoDao = RepoDao()):
        self.repo_dao = repo_dao

    async def get_all(self):
        repos = await self.repo_dao.get_all()
        return [RepoPublic.model_validate(repo) for repo in repos]

    async def get_by_id(self):
        pass

    async def delete(self):
        pass

    async def upsert(self):
        pass
