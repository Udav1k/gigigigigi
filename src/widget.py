"""
Модуль для работы с виджетом банковских операций.
Содержит функции для обработки данных карт/счетов и дат.
"""

from datetime import datetime

# Импортируем функции маскировки из соседнего модуля
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Обрабатывает информацию о картах и счетах, маскируя их номера.
    """
    # Добавляем проверку на тип данных и пустое значение
    if not isinstance(data, str) or not data:
        return "Ошибка: Некорректный формат данных"

    try:
        # Разделяем строку с конца на 2 части
        name_part, number_part = data.rsplit(maxsplit=1)

        # Выбираем алгоритм маскировки
        if name_part.lower().startswith("счет"):
            masked_number = get_mask_account(number_part)
        else:
            masked_number = get_mask_card_number(number_part)

        return f"{name_part} {masked_number}"

    except (ValueError, AttributeError):
        # Если в строке нет пробелов или произошла ошибка обработки
        return "Ошибка: Некорректный формат данных"


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой из формата ISO 8601 в формат ДД.ММ.ГГГГ.
    """
    # Проверка типа данных (важно для обработки None и чисел)
    if not isinstance(date_string, str):
        return "Ошибка: Некорректный формат даты"

    try:
        # Пытаемся преобразовать строку в объект datetime
        dt_object = datetime.fromisoformat(date_string)
        return dt_object.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        # Ловим ошибки формата строки или неверного типа аргумента
        return "Ошибка: Некорректный формат даты"


if __name__ == "__main__":
    # Блок демонстрации
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(get_date("2024-03-11T02:26:18.671407"))
