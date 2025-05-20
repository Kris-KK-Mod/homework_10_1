from datetime import datetime


def mask_account_card(data: str) -> str:
    """
    Принимает строку с типом и номером карты/счета, возвращает замаскированную строку.
    Форматы:
    - Карта: "Visa Platinum 7000792289606361" → "Visa Platinum 7000 79** **** 6361"
    - Счет (рус): "Счет 73654108430135874305" → "Счет **4305"
    - Счет (англ): "Account 12345678901234567890" → "Account **7890"
    """
    if not isinstance(data, str):
        return "Ошибка: входные данные должны быть строкой"

    parts = data.split()
    if len(parts) < 2:
        return "Ошибка: строка должна содержать тип и номер"

    name = " ".join(parts[:-1])
    number = parts[-1]

    # Для счетов (русских и английских)
    if name.lower() in ["счет", "account"]:
        if len(number) < 4:
            return "Ошибка: номер счёта должен содержать минимум 4 цифры"
        return f"{name} **{number[-4:]}"

    # Для карт
    digits = "".join(filter(str.isdigit, number))
    if len(digits) < 10:
        return "Ошибка: номер карты должен содержать минимум 10 цифр"
    return f"{name} {digits[:4]} {digits[4:6]}** **** {digits[-4:]}"


def get_date(date_str: str) -> str:
    """
    Принимает строку вида '2024-03-11T02:26:18.671407'
    Возвращает строку вида '11.03.2024'
    """
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return "Ошибка: неверный формат даты"
