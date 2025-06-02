# function/schedule_loader.py      логика получения расписания

from datetime import datetime

def get_today_schedule(file_path: str = "data/schedule.txt") -> str:

    day_index = datetime.today().weekday()
    days_list = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье"
    ]
    today_rus = days_list[day_index]

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        schedule = []
        in_today_block = False

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.endswith(":"):
                current_day = line.rstrip(":").strip()
                in_today_block = (current_day.lower() == today_rus.lower())
                continue

            if in_today_block:
                if line.endswith(":"):
                    break
                schedule.append(line)

        if not schedule:
            return f"📅 Сегодня: <b>{today_rus}</b>\nРасписание не найдено."

        result = f"📅 Сегодня: <b>{today_rus}</b>\n" + "\n".join(
            [f"{i+1}. {lesson}" for i, lesson in enumerate(schedule)]
        )
        return result

    except FileNotFoundError:
        return "Файл с расписанием не найден."


def get_schedule_by_day(day: str, file_path: str = "data/schedule.txt") -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        schedule = []
        in_day_block = False

        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.endswith(":"):
                in_day_block = (line[:-1].lower() == day.lower())
                continue
            if in_day_block:
                if line.endswith(":"):  # следующий день начался
                    break
                schedule.append(line)

        if not schedule:
            return f"На <b>{day}</b> расписание не найдено."

        result = f"📅 <b>{day}</b>\n" + "\n".join(
            [f"{i+1}. {lesson}" for i, lesson in enumerate(schedule)]
        )
        return result

    except FileNotFoundError:
        return "Файл с расписанием не найден."
