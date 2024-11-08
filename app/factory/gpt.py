from typing import Any, Final

import httpx
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion

from app.models.config import AppConfig

_LOCAL_ADDRESS: Final[str] = "0.0.0.0"


class GptClient:

    def __init__(self, config: AppConfig) -> None:
        self.gpt = AsyncOpenAI(
            api_key=config.common.gpt_token.get_secret_value(),
            http_client=httpx.AsyncClient(
                proxies=config.common.proxy,
                transport=httpx.AsyncHTTPTransport(
                    local_address=_LOCAL_ADDRESS,
                ),
            ),
        )

    async def response(
            self,
            *,
            question: str,
            role: str = "user",
            model: str = "gpt-4o",
            return_text: bool = False,
            data: list[dict[str, Any]] | None = None,
    ) -> ChatCompletion | str | Any:
        content = (
            f"{question}\n\n"
            f'если это не относится к спортивной тематике отправь '
            f'"Ваше сообщение не относится к спортивной тематике"'
        )
        messages = data if data else [{"role": role, "content": content}]

        response = await self.gpt.chat.completions.create(
            model=model,
            messages=messages,
        )
        if return_text:
            return response.choices[0].message.content
        return response
