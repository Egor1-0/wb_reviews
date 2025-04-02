from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from ..schemas.status import Status


class Participation(Base):
    __tablename__ = 'participations'

    promotion_id: Mapped[int] = mapped_column(ForeignKey('promotions.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    status: Mapped[Status] = mapped_column(default=Status.FIRST_STAGE)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    ended_at: Mapped[datetime | None]

    promotion: Mapped['Promotion'] = relationship(back_populates='participations', foreign_keys=[promotion_id])