# handlers/fsm_homework.py

from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import CallbackQuery
from function.homework_logic import get_homework_by_date
from keyboards.menu import get_main_keyboard

router = Router()

# 1. Описание состояний
class HomeworkDateInput(StatesGroup):
    waiting_for_date = State()

# 2. Обработка нажатия кнопки "ручной ввод"
@router.callback_query(F.data == "manual_date")
async def ask_for_date(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("📅 Введите дату в формате ДД.ММ.ГГГГ:")
    await state.set_state(HomeworkDateInput.waiting_for_date)
    await callback.answer()

# 3. Обработка текста — введённой вручную даты
@router.message(HomeworkDateInput.waiting_for_date)
async def process_date_input(message: Message, state: FSMContext):
    date_str = message.text.strip()
    result = get_homework_by_date(date_str)
    # невидимый символ + перенос разворачивает replay-меню даже при ошибочном вводе даты
    await message.answer("\n" + result, reply_markup=get_main_keyboard())  
    await state.clear()

