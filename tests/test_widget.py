import pytest

from src.widget import get_date, mask_account_card


# Тесты для маскировки (закрываем основные сценарии и ошибки)
@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", "Ошибка: Некорректный формат данных"),
        (None, "Ошибка: Некорректный формат данных"),
        ("Unknown 123", "Unknown Неверный формат номера карты"),
    ],
)
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected


# Тесты для даты (закрываем ветки try, except и проверку типа)
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2018-07-11T02:26:18.671407", "11.07.18"),
        ("2024-12-31", "31.12.24"),
        ("invalid-date", "Ошибка: Некорректный формат даты"),
        ("", "Ошибка: Некорректный формат даты"),
        (None, "Ошибка: Некорректный формат даты"),
        (12345, "Ошибка: Некорректный формат даты"),
    ],
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
