from pydantic import BaseModel, Field, Extra


class Card(BaseModel):
    title: str = Field(alias='name')
    brand: str
    article: int = Field(alias='id')

    class Config:
        extra = Extra.ignore
