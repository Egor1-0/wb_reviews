from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base


class User(Base):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(nullable=True)

    participations: Mapped['Participation'] = relationship(back_populates='user')