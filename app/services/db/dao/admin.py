from sqlalchemy.ext.asyncio import AsyncSession

from app.models.sql import AdminModel
from app.models.dataclasses import Admin
from app.services.db.repository import Repository


class AdminDAO:
    repository: Repository[AdminModel]

    __slots__ = ("repository",)

    def __init__(self, session: AsyncSession) -> None:
        self.repository = Repository(
            session=session,
            model=AdminModel,
        )

    async def add_admin(
            self,
            *,
            admin_id: int,
            name: str,
    ) -> None:
        await self.repository.insert(
            admin_id=admin_id,
            name=name,
        )
        await self.repository.commit()

    async def get_admin_by_id(
            self,
            admin_id: int,
    ) -> Admin | None:
        result_obj = await self.repository.get_by_where(
            AdminModel.admin_id == admin_id,
        )
        admin_info = result_obj.all()
        if admin_info:
            return Admin(*admin_info[0])
        return None



