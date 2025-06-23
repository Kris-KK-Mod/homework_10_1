import logging
from typing import Union

# Настройка логгера
masks_logger = logging.getLogger(__name__)


def mask_account_number(account_number: Union[str, None]) -> str:
    """
    Маскирует номер счета (видны только последние 4 цифры).
    Возвращает строку с ошибкой, если номер счета некорректен.
    """
    if account_number is None:
        error_msg = "Ошибка: номер счёта не может быть None"
        masks_logger.warning(error_msg)
        return error_msg

    try:
        digits = ''.join(c for c in str(account_number) if c.isdigit())

        if len(digits) < 4:
            error_msg = "Ошибка: номер счёта должен содержать минимум 4 цифры"
            masks_logger.warning(f"{error_msg}: {account_number}")
            return error_msg

        return "**" + digits[-4:]

    except Exception as e:
        error_msg = f"Ошибка при маскировке счета: {str(e)}"
        masks_logger.error(f"{error_msg}: {account_number}", exc_info=True)
        return error_msg


def mask_card_number(card_number: Union[str, None]) -> str:
    """
    Маскирует номер карты (видны первые 6 и последние 4 цифры).
    Возвращает строку с ошибкой, если номер карты некорректен.
    """
    if card_number is None:
        error_msg = "Ошибка: номер карты не может быть None"
        masks_logger.warning(error_msg)
        return error_msg

    try:
        digits = ''.join(c for c in str(card_number) if c.isdigit())

        if len(digits) < 10:
            error_msg = "Ошибка: номер карты должен содержать минимум 10 цифр"
            masks_logger.warning(f"{error_msg}: {card_number}")
            return error_msg

        if len(digits) != 16:
            error_msg = "Ошибка: номер карты должен содержать 16 цифр"
            masks_logger.warning(f"{error_msg}: {card_number}")
            return error_msg

        return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"

    except Exception as e:
        error_msg = f"Ошибка при маскировке карты: {str(e)}"
        masks_logger.error(f"{error_msg}: {card_number}", exc_info=True)
        return error_msg
