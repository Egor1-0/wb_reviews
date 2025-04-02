from pydantic import BaseModel


class Statistics(BaseModel):
    start: int = 0
    end: int = 0