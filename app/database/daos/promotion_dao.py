from typing import Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.daos.base import BaseDao, ModelType
from database.models import Promotion


class PromotionDao(BaseDao):
    model = Promotion

    @classmethod
    async def find_active_promotions(cls, session: AsyncSession) -> list[Type[ModelType]]:
        query = select(cls.model).where(cls.model.count > 0)
        res = await session.execute(query)
        return res.scalars().all()