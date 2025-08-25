from dataclasses import dataclass
from sqlalchemy import BigInteger, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.repository.entity.base_entity import BaseEntity


@dataclass
class RepoEntity(BaseEntity):
    __tablename__ = "repos"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    stargazers_count: Mapped[int] = mapped_column(Integer)
    forks_count: Mapped[int] = mapped_column(Integer)
    open_issues_count: Mapped[int] = mapped_column(Integer)
    watchers_count: Mapped[int] = mapped_column(Integer)
    tags: Mapped[str] = mapped_column(String(255), nullable=True)
    topics: Mapped[str] = mapped_column(String(255), nullable=True)
    owner: Mapped[str] = mapped_column(String(255))
