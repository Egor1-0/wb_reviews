from sqlalchemy.orm import Mapped

from .base import Base


class Promotion(Base):
    __tablename__ = 'promotions'

    name: Mapped[str]
    keywords: Mapped[str]
    count: Mapped[int]