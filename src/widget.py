from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Маскирует номер карты или счета."""
    if not isinstance(data, str) or not data:
        return "Ошибка: Некорректный формат данных"

    try:
        name_part, number_part = data.rsplit(maxsplit=1)
        if "счет" in name_part.lower():
            return f"{name_part} {get_mask_account(number_part)}"
        return f"{name_part} {get_mask_card_number(number_part)}"
    except (ValueError, AttributeError):
        return "Ошибка: Некорректный формат данных"


def get_date(date_string: str) -> str:
    """Преобразует дату в формат ДД.ММ.ГГГГ."""
    if not isinstance(date_string, str) or not date_string:
        return "Ошибка: Некорректный формат даты"

    try:
        dt_object = datetime.fromisoformat(date_string)
        # Обязательно %Y для формата 2018 (4 цифры)
        return dt_object.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return "Ошибка: Некорректный формат даты"
