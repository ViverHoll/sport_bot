from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import SportsmanModel
from app.db.repository import Repository
from app.entities.dataclasses import Sportsman


class SportsmanBase:
    repository: Repository[SportsmanModel]

    __slots__ = ("repository",)

    def __init__(self, *, session: AsyncSession) -> None:
        self.repository = Repository(
            session=session,
            model=SportsmanModel
        )

    async def add_sportsman(self, **values) -> None:
        await self.repository.insert(**values)
        await self.repository.commit()

    async def get_sportsman_by_id(self,
                                  sportsman_id: int
                                  ) -> Optional[Sportsman]:
        result_obj = await self.repository.get_by_where(
            SportsmanModel.sportsmen_id == sportsman_id
        )

        sportsman = result_obj.all()

        if sportsman:
            return Sportsman(*sportsman[0])
        return None

    async def get_athletes(self) -> list[Sportsman]:
        result_obj = await self.repository.get_by_where()




        athletes = result_obj.all()


        # for sportsman in xyi:
        #     athletes.append(
        #         Sportsman(*sportsman)
        #     )

        return [
            Sportsman(*sportsman)
            for sportsman in athletes
        ]
