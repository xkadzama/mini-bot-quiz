import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers.start import user


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('API'))
    dp = Dispatcher()
    dp.include_router(user, quiz)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())