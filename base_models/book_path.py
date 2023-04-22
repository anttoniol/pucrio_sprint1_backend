from pydantic import BaseModel, Field


class BookPath(BaseModel):
    id: int = Field(..., description = "Book ID")