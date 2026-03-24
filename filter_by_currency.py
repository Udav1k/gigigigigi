def card_number_generator(
    begin_card_number: Optional[int] = None, end_card_number: Optional[int] = None
) -> Generator[str, None, None]:
    """Функция генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Параметры: begin_card_number - начальный номер, end_card_number - конечный номер генерации."""

    if not isinstance(begin_card_number, int) or not isinstance(end_card_number, int):
        raise TypeError("Тип входного аргумента должен быть целым")

    if 0 < begin_card_number <= 9999999999999999 and 0 < end_card_number <= 9999999999999999:

        for num in range(begin_card_number, end_card_number + 1):
            number = str(num).zfill(16)
            formatted_number = f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
            yield formatted_number
    else:
        raise TypeError("Входные параметры вне диапазона")
