import logging
from typing import Type, Any

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

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
    async def get_statistics(cls, session: AsyncSession, promotion_id: int) -> Any:
        query_create = (
            select(
                func.date(Participation.created_at),
                func.count(Participation.id)
            )
            .where(Participation.promotion_id == promotion_id)
            .group_by(func.date(Participation.created_at))
            .order_by(func.date(Participation.created_at))
        )

        query_end = (
            select(
                func.date(Participation.ended_at),
                func.count(Participation.id)
            )
            .where(Participation.promotion_id == promotion_id)
            .group_by(func.date(Participation.ended_at))
            .order_by(func.date(Participation.ended_at))
        )

        res_create = (await session.execute(query_create)).all()
        res_end = (await session.execute(query_end)).all()
        return res_create, res_end