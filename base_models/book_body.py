from pydantic import BaseModel, Field


class BookBody(BaseModel):
    title: str = Field(..., min_length = 1, description = "Title")
    author: str = Field(..., min_length = 1, description = "Author")
    publication_date: str = Field(..., min_length = 1, description = "Publication Date")