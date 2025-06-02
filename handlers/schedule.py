# handlers/schedule.py             обрабатываем кнопки

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from function.schedule_loader import get_today_schedule, get_schedule_by_day
from keyboards.days import get_day_keyboard
from keyboards.menu import get_main_keyboard

router = Router()

@router.message(F.text == "🗓 Расписание")
async def choose_day(message: Message):
    await message.answer("Выбери день недели:", reply_markup=get_day_keyboard())

@router.callback_query(F.data == "day_today")            # Сегодня
async def send_today(callback: CallbackQuery):
    result = get_today_schedule()
    await callback.message.answer(result)
    await callback.answer()  # чтобы убрать "часики"

@router.callback_query(F.data.startswith("day_"))        # Дни недели
async def send_schedule_by_day(callback: CallbackQuery):
    day = callback.data[4:]  # обрезаем 'day_'
    result = get_schedule_by_day(day)
    await callback.message.answer(result)
    await callback.answer()  # чтобы убрать "часики"

@router.callback_query(F.data == "back_to_menu")         # Назад
async def back(callback: CallbackQuery):
    # Удаляем старое сообщение с inline-кнопками
    await callback.message.delete()
    # Отправляем обычное сообщение с replay-клавиатурой
    await callback.message.answer(text="📋 Главное меню:", reply_markup=get_main_keyboard())
    await callback.answer()  # чтобы убрать "часики"