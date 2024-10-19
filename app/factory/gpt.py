from typing import Any

import httpx
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion

from app.app_config import AppConfig


class GptClient:
    local_address = "0.0.0.0"

    def __init__(self, config: AppConfig) -> None:
        # proxy = FreeProxy().get()
        # print(proxy)
        self.gpt = AsyncOpenAI(
            api_key=config.common.gpt_token.get_secret_value(),
            http_client=httpx.AsyncClient(
                proxies=config.common.proxy,
                transport=httpx.HTTPTransport(
                    local_address=self.local_address
                )
            )
        )
        # print(self.gpt.models.list())

    async def response(
            self,
            *,
            question: str,
            role: str = "user",
            model: str = "gpt-4o",
            return_text: bool = False
    ) -> ChatCompletion | str | Any:
        content = (
            f"{question}\n\n"
            f'если это не относится к спортивной тематике отправь '
            f'"Ваше сообщение не относится к спортивной тематике"'
        )
        response = await self.gpt.chat.completions.create(
            messages=[
                {
                    "role": role,
                    "content": content
                }
            ],
            model=model,
        )
        if return_text:
            return response.choices[0].message.content
        return response
