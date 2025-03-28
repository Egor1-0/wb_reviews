from pydantic import BaseModel


class CreatePromotion(BaseModel):
    name: str
    keywords: str
    count: int