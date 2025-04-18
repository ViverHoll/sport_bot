from sqlalchemy.ext.asyncio import AsyncSession

from .sportsman import SportsmanDAO
from .user import UsersDAO
from .strength_indicators import StrengthIndicatorDAO
from .favorite import FavoriteDAO
from .gpt import GptDAO
from .admin import AdminDAO


class HolderDAO:
    users: UsersDAO
    athletes: SportsmanDAO
    strength_indicator: StrengthIndicatorDAO
    favorite: FavoriteDAO
    gpt: GptDAO
    admin: AdminDAO

    __slots__ = (
        "users",
        "athletes",
        "strength_indicator",
        "favorite",
        "gpt",
        "admin",
    )

    def __init__(self, *, session: AsyncSession) -> None:
        self.users = UsersDAO(session=session)
        self.athletes = SportsmanDAO(session=session)
        self.strength_indicator = StrengthIndicatorDAO(session=session)
        self.favorite = FavoriteDAO(session=session)
        self.gpt = GptDAO(session=session)
        self.admin = AdminDAO(session=session)
