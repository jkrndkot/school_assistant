# keyboards/days.py

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_day_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(text="📅 Сегодня", callback_data="day_today"),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_menu")
        ],
        [
            InlineKeyboardButton(text="Пн", callback_data="day_Понедельник"),
            InlineKeyboardButton(text="Вт", callback_data="day_Вторник"),
            InlineKeyboardButton(text="Ср", callback_data="day_Среда"),
            InlineKeyboardButton(text="Чт", callback_data="day_Четверг"),
            InlineKeyboardButton(text="Пт", callback_data="day_Пятница"),
            InlineKeyboardButton(text="Сб", callback_data="day_Суббота"),
            InlineKeyboardButton(text="🔴 Вс", callback_data="day_Воскресенье"),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)