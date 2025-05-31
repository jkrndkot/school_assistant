# handlers/start.py

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.menu import get_main_keyboard

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Привет! Я твой школьный ассистент.\n\nВот что я умею:",
        reply_markup=get_main_keyboard()
    )
