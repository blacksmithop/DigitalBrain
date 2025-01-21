from pydantic import BaseModel
from typing import Optional


class MediumArticle(BaseModel):
    title: str
    publication_date: str
    perma_link: str
    content: Optional[str] = None