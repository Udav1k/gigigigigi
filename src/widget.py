"""
Модуль для работы с виджетом банковских операций.
Содержит функции для обработки данных карт/счетов и дат.
"""

from datetime import datetime

# Импортируем функции маскировки из соседнего модуля
# Примечание: PyCharm может подсвечивать ошибку, если папка src не помечена как Source Root,
# но при запуске из корня проекта через python -m src.widget это сработает.
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Обрабатывает информацию о картах и счетах, маскируя их номера.

    Функция определяет тип (Карта или Счет) на основе входной строки
    и применяет соответствующую маску.

    Args:
        data (str): Строка вида 'Visa Platinum 7000792289606361' или 'Счет 73654108430135874305'.

    Returns:
        str: Строка с замаскированным номером, например:
             'Visa Platinum 7000 79** **** 6361' или 'Счет **4305'.
    """
    # Разделяем строку с конца на 2 части:
    # 1. Название (может содержать пробелы, например "Visa Platinum")
    # 2. Номер (последнее слово в строке)
    try:
        name_part, number_part = data.rsplit(maxsplit=1)
    except ValueError:
        # Если строку нельзя разделить (например, пришло только число или пустая строка)
        return "Ошибка: Некорректный формат данных"

    # Выбираем алгоритм маскировки
    if name_part.lower().startswith("счет"):
        masked_number = get_mask_account(number_part)
    else:
        masked_number = get_mask_card_number(number_part)

    return f"{name_part} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой из формата ISO 8601 в формат ДД.ММ.ГГГГ.

    Args:
        date_string (str): Дата в формате "YYYY-MM-DDTHH:MM:SS.mmmmmm".
                           Пример: "2024-03-11T02:26:18.671407"

    Returns:
        str: Дата в формате "DD.MM.YYYY".
    """
    try:
        # fromisoformat отлично справляется со стандартным форматом ISO
        dt_object = datetime.fromisoformat(date_string)
        return dt_object.strftime("%d.%m.%Y")
    except ValueError:
        return "Ошибка: Некорректный формат даты"


if __name__ == "__main__":
    # Блок демонстрации работы функций
    print("--- Тест обработки карт и счетов ---")
    inputs = [
        "Visa Platinum 7000792289606361",
        "Maestro 7000792289606361",
        "Счет 73654108430135874305",
        "НекорректныеДанные",
    ]

    for item in inputs:
        try:
            print(f"Вход: '{item}' -> Выход: '{mask_account_card(item)}'")
        except Exception as e:
            print(f"Ошибка при обработке '{item}': {e}")

    print("\n--- Тест обработки дат ---")
    test_date = "2024-03-11T02:26:18.671407"
    print(f"Вход: '{test_date}' -> Выход: '{get_date(test_date)}'")

    bad_date = "2024/03/11"
    print(f"Вход: '{bad_date}' -> Выход: '{get_date(bad_date)}'")
