from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import StrengthIndicatorsModel
from app.db.repository import Repository


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




