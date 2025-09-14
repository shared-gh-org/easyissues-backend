from abc import ABC
from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar, Type, Optional
import logging

from src.dependency.database import DatabaseSessionManager
from src.repository.entity.base_entity import BaseEntity
from sqlalchemy import Executable, Delete, Select, Update, Insert, delete, select


T = TypeVar("T", bound=BaseEntity)


class BaseDao(ABC):
    __abstract__ = True

    def __init__(self, entity_class: Type[T], session_manager: DatabaseSessionManager):
        self._entity_class = entity_class
        self._session_manager = session_manager

    async def get_all(self, db_session: Optional[AsyncSession] = None):
        try:
            statement = select(self._entity_class)
            results = await self.execute_query(statement, db_session)
            logging.info(
                f"Fetched {len(results)} record(s) from {self._entity_class.__tablename__}"
            )
            return results
        except Exception as e:
            logging.error(
                f"Error while fetching all records from {self._entity_class.__tablename__}: {e}"
            )
            raise

    async def get_by_id(self, id: int, db_session: Optional[AsyncSession] = None):
        try:
            statement = select(self._entity_class).where(self._entity_class.id == id)
            results = await self.execute_query(statement, db_session)
            logging.info(f"Fetched record with id {id}")
            return results[0]
        except Exception as e:
            logging.error(
                f"Error while fetching record with id {id} from" +
                f" {self._entity_class.__tablename__}: {e}"
            )
            raise

    async def delete(self, id: int, db_session: Optional[AsyncSession] = None) -> int:
        try:
            statement = delete(self._entity_class).where(self._entity_class.id == id)
            rowcount = await self.execute_query(statement, db_session)
            logging.info(
                f"Deleted {rowcount} record(s) from " +
                f"{self._entity_class.__tablename__} where id={id}"
            )
            return rowcount
        except Exception as e:
            logging.error(
                f"Error while deleting from {self._entity_class.__tablename__} where id={id}: {e}"
            )
            raise

    async def upsert(
        self, id: int, entity: BaseEntity, db_session: Optional[AsyncSession] = None
    ):
        try:
            existing = await self.get_by_id(id, db_session)
            if existing:
                for field, value in entity.__dict__.items():
                    if not field.startswith("_") and hasattr(existing, field):
                        setattr(existing, field, value)
                statement = (
                    Update(self._entity_class)
                    .where(self._entity_class.id == id)
                    .values(**entity.to_dict())
                )
                await self.execute_query(statement, db_session)
                logging.info(f"Updated {self._entity_class.__tablename__} with id {id}")
                return existing
            else:
                statement = Insert(self._entity_class).values(**entity.to_dict())
                await self.execute_query(statement, db_session)
                logging.info(
                    f"Inserted new {self._entity_class.__tablename__} with id {id}"
                )
                return entity
        except Exception as e:
            logging.error(
                f"Error while upserting {self._entity_class.__tablename__} with id {id}: {e}"
            )
            raise

    async def execute_query(
        self, query: Executable, db_session: Optional[AsyncSession] = None
    ):
        if db_session:
            return await self._execute(query, db_session)

        async with self._session_manager.get_db_session() as session:
            return await self._execute(query, session)

    async def _execute(self, query: Executable, session: AsyncSession):
        result = await session.execute(query)
        if isinstance(query, (Insert, Update, Delete)):
            await session.commit()
            return getattr(result, "rowcount", None)
        elif isinstance(query, Select):
            return result.scalars().all() if len(result.keys()) == 1 else result.all()
        return result
