from typing import TypeAlias

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


SessionPool: TypeAlias = async_sessionmaker[AsyncSession]

def create_engine(url, echo):
    return create_async_engine(
        url=url,
        echo=echo,
    )

def create_session_pool(*, url: URL, echo: bool = False) -> SessionPool:
    """Create session pool."""
    engine = create_engine(url, echo)
    return async_sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False,
        autocommit=False,
    )


# async def create_base(url, echo):
#     return BaseModel.metadata.create_all(
#         create_engine(url, echo)
#     )
