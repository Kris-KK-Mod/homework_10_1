from typing import Optional

from . import masks_logger


def mask_account_number(account_number: str) -> Optional[str]:
    """
    Маскирует номер счета (видны только последние 4 цифры).
    """
    try:
        if len(account_number) < 4:
            masks_logger.warning(f"Слишком короткий номер счета: {account_number}")
            return None

        masked = "**" + account_number[-4:]
        masks_logger.info(f"Успешно замаскирован номер счета: {account_number}")
        return masked

    except Exception as e:
        masks_logger.error(f"Ошибка при маскировке счета {account_number}: {str(e)}", exc_info=True)
        return None


def mask_card_number(card_number: str) -> Optional[str]:
    """
    Маскирует номер карты (видны первые 6 и последние 4 цифры).
    """
    try:
        if len(card_number) != 16:
            masks_logger.warning(f"Некорректная длина номера карты: {card_number}")
            return None

        masked = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        masks_logger.info(f"Успешно замаскирован номер карты: {card_number}")
        return masked

    except Exception as e:
        masks_logger.error(f"Ошибка при маскировке карты {card_number}: {str(e)}", exc_info=True)
        return None
