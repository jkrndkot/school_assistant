# function/joke_logic.py

import random

JOKES_FILE = "data/jokes.txt"

def get_random_joke() -> str:
    try:
        with open(JOKES_FILE, "r", encoding="utf-8") as f:
            jokes = [line.strip() for line in f if line.strip()]
        return random.choice(jokes) if jokes else "Файл с шутками пуст."
    except FileNotFoundError:
        return "Файл с шутками не найден."

