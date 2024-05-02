import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from Token import Token
from app.handlers import router
logging.basicConfig(level=logging.INFO)

async def main():
    dp=Dispatcher()
    bot = Bot(token=Token)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ =='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен!')