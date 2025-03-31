from sqlalchemy.orm import Mapped, relationship

from .base import Base


class Promotion(Base):
    __tablename__ = 'promotions'

    name: Mapped[str]
    keywords: Mapped[str]
    count: Mapped[int]

    participations: Mapped['Participation'] = relationship(back_populates='promotion')