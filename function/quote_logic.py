# function/quote_logic.py

import random

QUOTES_FILE = "data/quotes.txt"

def get_random_quote() -> str:
    try:
        with open(QUOTES_FILE, "r", encoding="utf-8") as f:
            quotes = [line.strip() for line in f if line.strip()]
        return random.choice(quotes) if quotes else "Файл с цитатами пуст."
    except FileNotFoundError:
        return "Файл с цитатами не найден."
