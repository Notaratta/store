from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from collections.abc import AsyncIterable





def new_session_maker() -> async_sessionmaker[AsyncSession]:
    database_uri = "sqlite+aiosqlite:///./store.db"
    engine = create_async_engine(
        database_uri,
        pool_size=15,
        max_overflow=15,
        # connect_args={
        #     "connect_timeout": 5,
        # },
    )
    return async_sessionmaker(engine, class_=AsyncSession, autoflush=False, expire_on_commit=False)


# def get_session_maker( ) -> async_sessionmaker[AsyncSession]:
#     return new_session_maker()

async def get_session(session_maker: async_sessionmaker[AsyncSession] = Depends(new_session_maker)) -> AsyncIterable[AsyncSession]:
    async with session_maker() as session:
        yield session


Base = declarative_base() 