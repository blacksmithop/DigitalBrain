from pydantic import BaseModel, Field
from typing import Optional


class GithubRepo(BaseModel):
    name: str
    clone_url: str

class GithubDownload(BaseModel):
    username: str
    fetch_private: bool = False
    token: str | None = Field(default=None, title="Github token (need for private repos)")