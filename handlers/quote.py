# handlers/quote.py

from aiogram import Router, F
from aiogram.types import Message
from function.quote_logic import get_random_quote
from keyboards.menu import get_main_keyboard

router = Router()

@router.message(F.text == "🎯 Цитата")
async def send_quote(message: Message):
    quote = get_random_quote()
    await message.answer(quote, reply_markup=get_main_keyboard())