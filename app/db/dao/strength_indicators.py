from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.sql import StrengthIndicatorsModel
from app.db.repository import Repository

from app.models.dataclasses import StrengthIndicatorType


class StrengthIndicatorDAO:
    repository: Repository[StrengthIndicatorsModel]

    __slots__ = ("repository",)

    def __init__(self, *, session: AsyncSession) -> None:
        self.repository = Repository(
            session=session,
            model=StrengthIndicatorsModel
        )

    async def add_strength_indicators(
            self,
            user_id: int,
            name: str,
            core: str
    ) -> None:
        await self.repository.insert(
            user_id=user_id,
            name=name,
            core=core
        )
        await self.repository.commit()

    async def get_all_strength_indicators(
            self,
            user_id: int
    ) -> list[StrengthIndicatorType] | None:
        result_obj = await self.repository.get_by_where(
            StrengthIndicatorsModel.user_id == user_id
        )
        parameters = result_obj.all()
        if parameters:
            return [
                StrengthIndicatorType(*p)
                for p in parameters
            ]
        return None

    async def update_by_exercise_id(
            self,
            user_id: int,
            exercise_id: int,
            **values: Any
    ) -> None:

        # думаю тут можно убрать юзер айди, так как у всех упражнений и так уникальный айди
        await self.repository.update_by_where(
            StrengthIndicatorsModel.user_id == user_id,
            StrengthIndicatorsModel.id == exercise_id,
            **values
        )
        await self.repository.commit()

    async def get_by_id(
            self,
            exercise_id: int
    ) -> StrengthIndicatorType | None:
        result_obj = await self.repository.get_by_where(
            StrengthIndicatorsModel.id == exercise_id
        )
        exercise = result_obj.all()
        if exercise:
            return StrengthIndicatorType(*exercise[0])
        return None
