from __future__ import annotations

from typing import Any, TypeVar, TYPE_CHECKING, Generic

from sqlalchemy import insert, select, update, CursorResult, Result, delete

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

from app.models.sql import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)


class Repository(Generic[ModelType]):
    session: AsyncSession
    model: type[ModelType]

    __slots__ = ("session", "model")

    def __init__(
            self,
            *,
            session: AsyncSession,
            model: type[ModelType]
    ) -> None:
        self.session = session
        self.model = model

    async def insert(self, **values: Any) -> CursorResult:
        query = insert(self.model).values(**values)
        return await self.session.execute(query)

    async def get_by_where(self, *whereclause) -> Result[Any]:
        query = select("*").select_from(self.model)

        if whereclause:
            query = query.where(*whereclause)

        return await self.session.execute(query)

    async def update_by_where(self, *whereclause: Any, **values: Any) -> Result[Any]:
        stmt = update(self.model).values(**values).returning(self.model)
        if whereclause:
            stmt = stmt.where(*whereclause)
        return await self.session.execute(stmt)

    async def delete_by_where(self, *whereclause: Any) -> Result[Any]:
        stmt = delete(self.model).where(*whereclause)
        return await self.session.execute(stmt)

    async def commit(self) -> None:
        return await self.session.commit()
