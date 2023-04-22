from pydantic import BaseModel, Field


class BookQuery(BaseModel):
    id: int = Field(None, description = "Book ID")
    title: str = Field(None, description = "Title")
    author: str = Field(None, description = "Author")
    publication_date: str = Field(None, description = "Publication Date")

    def get_filled_params(self):
        filled_params = dict()
        params = self.dict()
        for param, value in params.items():
            if value is not None:
                filled_params[param] = value
        return filled_params