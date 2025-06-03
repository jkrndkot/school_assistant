# handlers/joke.py

from aiogram import Router, F
from aiogram.types import Message
from function.joke_logic import get_random_joke
from keyboards.menu import get_main_keyboard

router = Router()

@router.message(F.text == "😂 Шутка от училки")
async def send_joke(message: Message):
    joke = get_random_joke().replace("\\n", "\n")
    await message.answer(joke, reply_markup=get_main_keyboard())
