# keyboards/homework_buttons.py

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta

def get_homework_inline_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📅 Выбрать дату", callback_data="choose_hw_date")]
        ]
    )

def get_date_choice_keyboard():
    base_date = datetime.today()
    buttons = []

    for i in range(1, 4):
        d = base_date + timedelta(days=i)
        text = d.strftime("%d.%m.%Y")
        buttons.append(InlineKeyboardButton(text=text, callback_data=f"hw_date_{text}"))

    keyboard = [
        buttons,
        [InlineKeyboardButton(text="🖊️ Выбрать дату вручную", callback_data="manual_date")]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


