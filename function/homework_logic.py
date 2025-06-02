# function/homework_logic.py  

from datetime import datetime

def get_today_homework(file_path: str = "data/homework.txt") -> str:
    today = datetime.today().strftime("%d.%m.%Y")  # → "29.05.2025"   # Например: "29 мая 2025"
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f]

        homework = []
        in_today_block = False

        for line in lines:
            if not line:
                continue

            if line.endswith(":"):
                current_day = line.rstrip(":").strip().lower()
                in_today_block = (current_day == today.lower())
                continue

            if in_today_block:
                if line.endswith(":"):  # начало нового дня
                    break
                homework.append(line)

        if not homework:
            return f"{today}\n📚 Домашка не найдена."

        result = f"{today}\n📚 Домашние задания:\n\n" + "\n".join(
            [f"{i+1}. {task}" for i, task in enumerate(homework)]
        )
        return result

    except FileNotFoundError:
        return "Файл с домашкой не найден."

def get_homework_by_date(date_str: str) -> str:
    """
    Получает домашку по дате. Формат даты: 29.05.2025
    """
    try:
        with open("data/homework.txt", "r", encoding="utf-8") as f:
            lines = f.read().splitlines()

        result_lines = []
        collecting = False
        for line in lines:
            if line.strip() == f"{date_str}:":
                collecting = True
                result_lines.append(f"{date_str}\n📚 Домашние задания:")
                continue
            if collecting:
                if line.strip() == "":
                    break
                result_lines.append(line)
        return "\n".join(result_lines) if result_lines else "На эту дату ничего не найдено."
    except FileNotFoundError:
        return "Файл с домашками не найден."
