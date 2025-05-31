# main.py

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from config import TOKEN
from handlers import start, schedule, homework, fsm_homework, quote, joke

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()
dp.include_router(start.router)
dp.include_router(schedule.router)
dp.include_router(homework.router)
dp.include_router(fsm_homework.router)
dp.include_router(quote.router)    
dp.include_router(joke.router)

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())