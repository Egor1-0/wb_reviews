from pydantic import BaseModel

from .status import Status


class CreateParticipation(BaseModel):
    promotion_id: int
    user_id: int
    status: Status
