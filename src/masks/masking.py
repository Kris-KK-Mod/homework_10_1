def get_mask_card_number(card_number: str) -> str:
    if not isinstance(card_number, str):
        return "Ошибка: номер карты должен быть строкой"
    digits = "".join(c for c in card_number if c.isdigit())
    if len(digits) < 10:
        return "Ошибка: номер карты должен содержать минимум 10 цифр"
    first_six = digits[:6]
    last_four = digits[-4:]
    return f"{first_six[:4]} {first_six[4:6]}** **** {last_four}"


def get_mask_account(account_number: str) -> str:
    if not isinstance(account_number, str):
        return "Ошибка: номер счёта должен быть строкой"
    digits = "".join(c for c in account_number if c.isdigit())
    if len(digits) < 4:
        return "Ошибка: номер счёта должен содержать минимум 4 цифры"
    last_four = digits[-4:]
    return f"**{last_four}"
