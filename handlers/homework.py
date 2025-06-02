# handlers/homework.py

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from function.homework_logic import get_today_homework, get_homework_by_date
from keyboards.homework_buttons import get_homework_inline_keyboard, get_date_choice_keyboard

router = Router()

@router.message(F.text == "📚 Домашка")
async def show_homework(message: Message):
    result = get_today_homework()
    await message.answer(result, reply_markup=get_homework_inline_keyboard())

@router.callback_query(F.data == "choose_hw_date")         # Выбрать дату домашки
async def choose_hw_date(callback: CallbackQuery):
    await callback.message.answer("📅 Выберите дату:", reply_markup=get_date_choice_keyboard())
    await callback.answer()

@router.callback_query(F.data.startswith("hw_date_"))      # Выбрать конкретную дату домашки из трёх
async def show_homework_by_date(callback: CallbackQuery):
    date_str = callback.data.removeprefix("hw_date_")
    result = get_homework_by_date(date_str)
    await callback.message.answer(result)
    await callback.answer()