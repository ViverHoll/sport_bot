from sqlalchemy.ext.asyncio import AsyncSession

from app.services.db.repository import Repository
from app.models.sql import GptQueryModel
from app.models.dataclasses import GptQueryType


class LikeDAO:
    repository: Repository[GptQueryModel]

    __slots__ = ("repository",)

    def __init__(self, session: AsyncSession) -> None:
        self.repository = Repository(
            session=session,
            model=GptQueryModel,
        )

    async def add_query(
            self,
            *,
            user_id: int,
            role: str,
            content: str,
    ) -> None:
        await self.repository.insert(
            user_id=user_id,
            role=role,
            content=content,
        )
        await self.repository.commit()

    async def get_all_query(
            self,
            user_id: int,
    ) -> list[GptQueryType] | None:
        result_obj = await self.repository.get_by_where(
            GptQueryModel.user_id == user_id,
        )
        requests = result_obj.all()
        if requests:
            return [
                GptQueryType(*r)
                for r in requests
            ]
        return None



