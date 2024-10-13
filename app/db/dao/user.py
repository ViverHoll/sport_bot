from typing import Any, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import UserModel
from app.db.repository import Repository
from app.entities.dataclasses import UserType


class UsersBase:
    repository: Repository[UserModel]

    __slots__ = ("repository",)

    def __init__(self, *, session: AsyncSession) -> None:
        self.repository = Repository(
            session=session,
            model=UserModel
        )

    async def add_user(self, **values) -> None:
        await self.repository.insert(**values)
        await self.repository.commit()

    async def get_user(self, user_id: int) -> Optional[UserModel]:
        result_obj = await self.repository.get_by_where(
            UserModel.user_id == user_id
        )
        user = result_obj.all()

        if user:
            return UserType(*user[0])
            # return user
        return None

    async def update_user(self, user_id: int, **values: Any) -> None:
        await self.repository.update_by_where(
            UserModel.user_id == user_id,
            **values
        )
        await self.repository.commit()




