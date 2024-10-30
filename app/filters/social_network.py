from typing import Any

from aiogram.filters import Filter
from aiogram.types import Message

from app.db import HolderDAO
from app.models.dataclasses import UserType


class UserRegSocialNetwork(Filter):
    """
    Класс-фильтр который проверяет регистрацию пользователя в социальной сети.
    Если есть - то пропустит.
    Если нет - то попросит зарегистрироваться.
    """

    async def __call__(
            self,
            message: Message,
            db: HolderDAO,
            **_kwargs: Any,
    ) -> None | UserType:
        return await db.social_network.get_user_by_id(
            user_id=message.from_user.id,
        )
