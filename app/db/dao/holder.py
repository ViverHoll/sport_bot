from sqlalchemy.ext.asyncio import AsyncSession

from .sportsman import SportsmanBase
from .user import UsersBase
from .sport_food import SportFoodBase
from .post import PostDAO
from .social_network import SocialNetworkDAO


class HolderDAO:
    users: UsersBase
    athletes: SportsmanBase
    sport_food: SportFoodBase
    post: PostDAO
    social_network: SocialNetworkDAO

    __slots__ = (
        "users",
        "athletes",
        "sport_food",
        "post",
        "social_network"
    )

    def __init__(self, *, session: AsyncSession) -> None:
        self.users = UsersBase(session=session)
        self.athletes = SportsmanBase(session=session)
        self.sport_food = SportFoodBase(session=session)
        self.post = PostDAO(session=session)
        self.social_network = SocialNetworkDAO(session=session)
