from pydantic import BaseModel
from typing import Optional


class Repo(BaseModel):
    name: str
    description: Optional[str] = None
    stargazers_count: int
    forks_count: int
    open_issues_count: int
    watchers_count: int
    tags: Optional[str] = None
    topics: Optional[str] = None
    owner: str

    model_config = {"from_attributes": True}


class RepoPublic(Repo):
    id: int


class RepoUpdate(Repo):
    pass


class RepoCreate(Repo):
    pass
