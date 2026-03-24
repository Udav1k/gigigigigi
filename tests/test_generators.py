import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод 1"},
        {"id": 2, "operationAmount": {"currency": {"code": "RUB"}}, "description": "Перевод 2"},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод 3"},
    ]


def test_filter_by_currency(sample_transactions):
    usd_tx = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_tx) == 2
    assert usd_tx[0]["id"] == 1

    rub_tx = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(rub_tx) == 1

    eur_tx = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(eur_tx) == 0

    empty_tx = list(filter_by_currency([], "USD"))
    assert len(empty_tx) == 0


def test_transaction_descriptions(sample_transactions):
    desc = list(transaction_descriptions(sample_transactions))
    assert desc == ["Перевод 1", "Перевод 2", "Перевод 3"]

    empty_desc = list(transaction_descriptions([]))
    assert empty_desc == []


def test_card_number_generator():
    cards = list(card_number_generator(1, 3))
    assert cards == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]

    edge_case = list(card_number_generator(9999999999999999, 9999999999999999))
    assert edge_case == ["9999 9999 9999 9999"]
