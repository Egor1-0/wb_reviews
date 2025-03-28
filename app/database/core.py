from sqlalchemy.ext.asyncio import async_sessionmaker as async_sessionmaker_, create_async_engine

from config import config

engine = create_async_engine(config.database.create_url())

async_sessionmaker = async_sessionmaker_(engine)
