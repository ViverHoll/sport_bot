import asyncio

from app.utils import configure_logging
from app.factory import create_app_config, create_bot, create_dispatcher


async def main() -> None:
    configure_logging()

    config = create_app_config()

    bot = create_bot(config)
    dp = await create_dispatcher(config)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
