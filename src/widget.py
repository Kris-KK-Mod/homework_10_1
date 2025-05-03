from src.masks.masking import get_mask_account, get_mask_card_number

def mask_account_card(data: str) -> str:
    """
    Принимает строку с типом и номером карты или счета, возвращает строку с замаскированным номером.
    Примеры:
    - 'Visa Platinum 7000792289606361'
    - 'Счет 73654108430135874305'
    """
    if not isinstance(data, str):
        return "Ошибка: входные данные должны быть строкой"

    parts = data.split()
    if len(parts) < 2:
        return "Ошибка: строка должна содержать тип и номер"

    name = " ".join(parts[:-1])  # Тип карты или слово "Счет"
    number = parts[-1]           # Сам номер

    if name.lower().startswith("счет"):
        masked = get_mask_account(number)
        return f"{name} {masked}"
    else:
        masked = get_mask_card_number(number)
        return f"{name} {masked}"
