from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repository import Repository
from app.db.models import LikeModel
from app.entities.dataclasses import LikeType


class LikeDAO:
    repository: Repository[LikeModel]

    __slots__ = ("repository",)

    def __init__(self, session: AsyncSession) -> None:
        self.repository = Repository(
            session=session,
            model=LikeModel
        )

    async def add_like(
            self,
            *,
            user_id: int,
            post_id: int
    ) -> None:
        await self.repository.insert(
            user_id=user_id,
            post_id=post_id
        )
        await self.repository.commit()

    async def get_like_by_ids(
            self,
            user_id: int,
            post_id: int
    ) -> LikeType | None:
        result_obj = await self.repository.get_by_where(
            LikeModel.user_id == user_id,
            LikeModel.post_id == post_id
        )
        like_info = result_obj.all()
        if like_info:
            return LikeType(*like_info[0])
        return None

    async def delete_like(
            self,
            user_id: int,
            post_id: int
    ) -> None:
        await self.repository.delete_by_where(
            LikeModel.user_id == user_id,
            LikeModel.post_id == post_id
        )
        await self.repository.commit()
