# Импортируем наши функции из модуля masks пакета src
from src.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    # Пример номеров для проверки
    card_number = "7000792289606361"
    account_number = "73654108430135874305"

    # Вызываем функции и выводим результат
    print(f"Номер карты: {get_mask_card_number(card_number)}")
    print(f"Номер счета: {get_mask_account(account_number)}")