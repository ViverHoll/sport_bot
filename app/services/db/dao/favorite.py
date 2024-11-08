from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.sql import FavoriteModel
from app.services.db.repository import Repository
from app.models.dataclasses import FavoriteType


class FavoriteDAO:
    repository: Repository[FavoriteModel]

    __slots__ = ("repository",)

    def __init__(self, *, session: AsyncSession) -> None:
        self.repository = Repository(
            session=session,
            model=FavoriteModel,
        )

    async def add_favorite(
            self,
            user_id: int,
            sportsman_id: int,
    ) -> None:
        """Add new favorite user."""
        await self.repository.insert(
            user_id=user_id,
            sportsman_id=sportsman_id,
        )
        await self.repository.commit()

    async def get_all_favorites(self, user_id: int) -> list[FavoriteType] | None:
        """Get all favorites."""
        result_obj = await self.repository.get_by_where(
            FavoriteModel.user_id == user_id,
        )
        favorites = result_obj.all()
        if favorites:
            return [
                FavoriteType(*favorite)
                for favorite in favorites
            ]
        return None

    async def get_favorite_by_sportsman_id(
            self,
            sportsman_id: int,
            user_id: int,
    ) -> FavoriteType | None:

        result_obj = await self.repository.get_by_where(
            FavoriteModel.user_id == user_id,
            FavoriteModel.sportsman_id == sportsman_id,
        )
        favorite = result_obj.all()
        if favorite:
            return FavoriteType(*favorite[0])
        return None

    async def delete_favorite(
            self,
            user_id: int,
            sportsman_id: Optional[int] = None,
    ) -> None:
        """Delete favorite."""
        await self.repository.delete_by_where(
            FavoriteModel.user_id == user_id,
            FavoriteModel.sportsman_id == sportsman_id,
        )

        await self.repository.commit()
