def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты:
    оставляет открытыми первые 6 и последние 4 цифры,
    остальные заменяет на символы 'X'.
    Пример: '1234 56XX XXXX 0000'
    """
    if not (isinstance(card_number, str) and card_number.isdigit() and len(card_number) == 16):
        return "Неверный формат номера карты"

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета:
    оставляет открытыми последние 4 цифры,
    остальные заменяет на символы 'X'.
    Пример: '**XXXXXX0000'
    """
    if not (isinstance(account_number, str) and account_number.isdigit() and len(account_number) >= 4):
        return "Неверный формат номера счета"

    return f"**{account_number[-4:]}"
