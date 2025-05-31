# keyboards/menu.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    kb = [
        [KeyboardButton(text="🗓 Расписание"), KeyboardButton(text="📚 Домашка")],
        [KeyboardButton(text="🎯 Цитата"), KeyboardButton(text="😂 Шутка от училки")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


