from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.sql import SportsmanModel
from app.services.db.repository import Repository
from app.models.dataclasses import Sportsman


class SportsmanDAO:
    repository: Repository[SportsmanModel]

    __slots__ = ("repository",)

    def __init__(self, *, session: AsyncSession) -> None:
        self.repository = Repository(
            session=session,
            model=SportsmanModel,
        )

    async def add_sportsman(
            self,
            *,
            name: str,
            surname: str,
            description: str,
            photo: str,
            nickname: str | None,
            exercises: str | None,
            food: str | None,
            music: str | None,
    ) -> None:
        await self.repository.insert(
            name=name,
            surname=surname,
            full_name=f"{name} {surname}",
            description=description,
            photo=photo,
            nickname=nickname,
            exercises=exercises,
            food=food,
            music=music,
        )
        await self.repository.commit()

    async def get_sportsman_by_id(self,
                                  sportsman_id: int,
                                  ) -> Optional[Sportsman]:
        result_obj = await self.repository.get_by_where(
            SportsmanModel.id == sportsman_id,
        )

        sportsman = result_obj.all()

        if sportsman:
            return Sportsman(*sportsman[0])
        return None

    async def get_athletes(self) -> list[Sportsman]:
        result_obj = await self.repository.get_by_where()
        athletes = result_obj.all()

        return [
            Sportsman(*sportsman)
            for sportsman in athletes
        ]

    async def get_sportsman_by_name(self, sportsman_name: str) -> Sportsman | None:
        result_obj = await self.repository.get_by_where(
            SportsmanModel.name == sportsman_name,
        )

        sportsman = result_obj.all()

        if sportsman:
            return Sportsman(*sportsman[0])
        return None

    async def get_sportsman_by_surname(self, sportsman_surname: str) -> Sportsman | None:
        result_obj = await self.repository.get_by_where(
            SportsmanModel.surname == sportsman_surname,
        )

        sportsman = result_obj.all()

        if sportsman:
            return Sportsman(*sportsman[0])
        return None
