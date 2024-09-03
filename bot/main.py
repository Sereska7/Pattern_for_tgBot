import asyncio
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from bot.core.config import settings

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


async def main():
    load_dotenv()
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        print("Bot online")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot offline")
