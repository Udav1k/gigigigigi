from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str = "USD") -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по заданной валюте."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Возвращает описание каждой транзакции."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера карт в заданном диапазоне в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        formatted = f"{number:016d}"
        yield f"{formatted[:4]} {formatted[4:8]} {formatted[8:12]} {formatted[12:]}"
