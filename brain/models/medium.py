from pydantic import BaseModel

class MediumArticle(BaseModel):
    title: str
    publication_date: str
    perma_link: str