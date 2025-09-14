from src.utils.decorators import singleton
from src.repository.dao.base_dao import BaseDao
from src.repository.entity.db_entities import RepoEntity
from src.dependency.database import DatabaseSessionManager, sessionmanager


@singleton
class RepoDao(BaseDao):
    def __init__(self, session_manager: DatabaseSessionManager = sessionmanager):
        super().__init__(entity_class=RepoEntity, session_manager=session_manager)
