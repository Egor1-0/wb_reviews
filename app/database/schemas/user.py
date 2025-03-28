from pydantic import BaseModel


class CreateUser(BaseModel):
    id: int