import logging
from typing import Type, TypeVar

from pydantic import BaseModel
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseDao:
    model: Type[ModelType]

    @classmethod
    async def create(cls, session: AsyncSession, obj: BaseModel | dict) -> Type[ModelType]:
        if not isinstance(obj, dict):
            obj = obj.model_dump(exclude_unset=True)
        model_in = cls.model(**obj)
        session.add(model_in)
        await session.commit()
        await session.refresh(model_in)
        return model_in

    @classmethod
    async def find_by_id(cls, session: AsyncSession, model_id: int) -> Type[ModelType]:
        query = select(cls.model).where(cls.model.id == model_id)
        res = await session.execute(query)

        return res.scalar()

    @classmethod
    async def find_all_by_filters(cls, session: AsyncSession, filters: dict | BaseModel) -> list[Type[ModelType]]:
        if not isinstance(filters, dict):
            filters = filters.model_dump(exclude_unset=True)
        query = select(cls.model).filter_by(**filters)
        res = await session.execute(query)

        return res.scalars().all()

    @classmethod
    async def find_one_by_filters(cls, session: AsyncSession, filters: dict | BaseModel) -> Type[ModelType]:
        if not isinstance(filters, dict):
            filters = filters.model_dump(exclude_unset=True)
        query = select(cls.model).filter_by(**filters)
        res = await session.execute(query)

        return res.scalar()

    @classmethod
    async def find_all(cls, session: AsyncSession) -> list[Type[ModelType]]:
        query = select(cls.model)
        res = await session.execute(query)

        return res.scalars().all()

    @classmethod
    async def update(cls, session: AsyncSession, filters: dict | BaseModel, values: dict | BaseModel) -> Type[ModelType]:
        if not isinstance(filters, dict):
            filters = filters.model_dump(exclude_unset=True)
        if not isinstance(values, dict):
            values = values.model_dump(exclude_unset=True)
        query = update(cls.model).filter_by(**filters).values(**values)
        await session.execute(query)
        await session.commit()

    @classmethod
    async def delete_by_id(cls, session: AsyncSession, model_id: int) -> None:
        query = delete(cls.model).where(cls.model.id == model_id)
        await session.execute(query)
        await session.commit()
