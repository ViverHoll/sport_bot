from typing import Any


async def get_subscribes(
        **_kwargs: Any
) -> dict[str, list[tuple[str, int]]]:
    return {
        "subscribes": [("Новичок", 1),
                       ("Опытный", 2),
                       ("Профессионал", 3)]
    }


async def get_terms(
        **_kwargs: Any
) -> dict[str, list[tuple[str, int]]]:
    return {
        "terms": [
            ("1 день", 1),
            ("1 неделя", 2),
            ("1 месяц", 3),
            ("3 месяца", 4),
            ("6 месяцев", 5),
            ("12 месяцев", 6),
        ]
    }
