import logging
from typing import Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from database.daos.base import BaseDao, ModelType
from database.models import Participation
from database.schemas.status import Status


class ParticipationDao(BaseDao):
    model = Participation

    @classmethod
    async def find_active_promotions(cls, session: AsyncSession, user_id: int) -> list[Type[ModelType]]:
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
