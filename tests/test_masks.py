import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("", "Неверный формат номера карты"),
        ("123", "Неверный формат номера карты"),
    ],
)
def test_get_mask_card_number(card, expected):
    assert get_mask_card_number(card) == expected


@pytest.mark.parametrize(
    "acc, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345", "**2345"),
        ("12", "Неверный формат номера счета"),
    ],
)
def test_get_mask_account(acc, expected):
    assert get_mask_account(acc) == expected
