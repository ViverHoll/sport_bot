from typing import Any


async def get_pay_url(
        *_: Any,
        **__: Any
) -> dict[str, str]:

    return {"pay_url": "https://google.com"}
