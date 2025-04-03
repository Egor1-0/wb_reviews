import logging
from typing import Type, Any

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.util import await_only

from database.daos.base import BaseDao, ModelType
from database.models import Participation, Promotion
from database.schemas.status import Status


class ParticipationDao(BaseDao):
    model = Participation

    @classmethod
    async def find_active_participations(cls, session: AsyncSession, user_id: int) -> list[Type[ModelType]]:
        query = (select(cls.model).where(cls.model.user_id == user_id,
                                         cls.model.status.in_([Status.FIRST_STAGE, Status.SECOND_STAGE]))
                 .options(joinedload(cls.model.promotion)))
        res = await session.execute(query)
        return res.scalars().all()

    @classmethod
    async def find_by_id_with_promotion(cls, session: AsyncSession, model_id: int) -> Type[ModelType]:
        query = select(cls.model).where(cls.model.id == model_id).options(joinedload(cls.model.promotion))
        res = await session.execute(query)
        return res.scalar()

    @classmethod
    async def get_statistics(cls, session: AsyncSession) -> Any:
        query = (
            select(Participation)
            .order_by(Participation.created_at)
            .options(joinedload(Participation.promotion),
                     joinedload(Participation.user)))
        result = await session.execute(query)
        return result.scalars().all()
