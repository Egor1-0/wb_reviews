from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from ..schemas.status import Status


class Participation(Base):
    __tablename__ = 'participations'

    promotion_id: Mapped[int] = mapped_column(ForeignKey('promotions.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    status: Mapped[Status] = mapped_column(default=Status.FIRST_STAGE)

    promotion: Mapped['Promotion'] = relationship(back_populates='participations', foreign_keys=[promotion_id])