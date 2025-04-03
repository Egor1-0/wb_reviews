from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Texts(Base):
    __tablename__ = 'texts'

    start_text: Mapped[str] = mapped_column(String, default='Стартовый текст')