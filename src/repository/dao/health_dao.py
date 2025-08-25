from sqlalchemy import text
from src.repository.dao.base_dao import BaseDao
from src.utils.constants import STATUSDOWN, STATUSUP
from src.dependency.database import DatabaseSessionManager, sessionmanager


class HealthDao(BaseDao):
    def __init__(self, session_manager: DatabaseSessionManager = sessionmanager):
        super().__init__(entity_class=None, session_manager=session_manager)

    async def get_health_metrics(self):
        query = text("SELECT 1")
        result = await self.execute_query(query)

        sessions = await self.execute_query(
            text("SELECT COUNT(*) FROM pg_stat_activity WHERE state = 'active'")
        )
        active_sessions = sessions.scalar_one()

        db_size = await self.execute_query(
            text("SELECT pg_size_pretty(pg_database_size(current_database()))")
        )
        size = db_size.scalar_one()

        return {
            "status": STATUSUP if result else STATUSDOWN,
            "sessions": active_sessions,
            "disk": size,
        }
