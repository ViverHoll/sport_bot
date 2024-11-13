from typing import Any, Optional

from aiogram.filters import Filter

from app.services.db import Database


class AdminFilter(Filter):
    """Класс-фильтр, проверяющий, является ли пользователь админом."""

    async def __call__(
            self,
            message: Any,
            db: Database,
            **_kwargs: Any,
    ) -> Optional[Any]:
        """Проверка на админа."""
        return await db.admin.get_admin_by_id(
            admin_id=message.from_user.id,
        )
