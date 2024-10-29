from typing import Optional, Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repository import Repository
from app.models.sql import PostModel

from app.models.dataclasses import PostType


class PostDAO:
    repository: Repository[PostModel]

    __slots__ = ("repository",)

    def __init__(self, session: AsyncSession) -> None:
        self.repository = Repository(
            session=session,
            model=PostModel,
        )

    async def add_post(
            self,
            post_from_user: int,
            media: str,
            description: str,
            tags: Optional[str] = None,
    ) -> None:
        await self.repository.insert(
            post_from_user=post_from_user,
            media=media,
            description=description,
            tags=tags,
        )
        await self.repository.commit()

    async def get_post_by_id(self, post_id: int) -> Optional[PostType]:
        result_obj = await self.repository.get_by_where(
            PostModel.post_id == post_id,
        )
        post = result_obj.all()
        if post:
            return PostType(*post[0])
        return None

    async def get_all_posts(self, user_id: int | None = None) -> list[PostModel] | list:
        if not user_id:
            result_obj = await self.repository.get_by_where()
        else:
            result_obj = await self.repository.get_by_where(
                PostModel.post_from_user == user_id,
            )
        posts = result_obj.all()

        return [
            PostType(*post)
            for post in posts
        ]

    async def update_post_by_id(self, post_id: int, **values: Any) -> None:
        await self.repository.update_by_where(
            PostModel.post_id == post_id,
            **values,
        )
        await self.repository.commit()

    async def delete_post(self, post_id: int) -> None:
        await self.repository.delete_by_where(
            PostModel.post_id == post_id,
        )
        await self.repository.commit()
