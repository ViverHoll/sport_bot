from sqlalchemy.ext.asyncio import AsyncSession

from .sportsman import SportsmanDAO
from .user import UsersDAO
from .sport_food import SportFoodDAO
from .post import PostDAO
from .social_network import SocialNetworkDAO
from .strength_indicators import StrengthIndicatorDAO
from .like import LikeDAO


class HolderDAO:
    users: UsersDAO
    athletes: SportsmanDAO
    sport_food: SportFoodDAO
    post: PostDAO
    social_network: SocialNetworkDAO
    strength_indicator: StrengthIndicatorDAO
    like: LikeDAO

    __slots__ = (
        "users",
        "athletes",
        "sport_food",
        "post",
        "social_network",
        "strength_indicator",
        "like"
    )

    def __init__(self, *, session: AsyncSession) -> None:
        self.users = UsersDAO(session=session)
        self.athletes = SportsmanDAO(session=session)
        self.sport_food = SportFoodDAO(session=session)
        self.post = PostDAO(session=session)
        self.social_network = SocialNetworkDAO(session=session)
        self.strength_indicator = StrengthIndicatorDAO(session=session)
        self.like = LikeDAO(session=session)
