from src.masks.masks import get_mask_account
from src.masks.masks import get_mask_card_number


def mask_input():
    print("Что вы хотите маскировать?")
    print("1 — Номер карты")
    print("2 — Номер счёта")
    choice = input("Введите 1 или 2: ")

    if choice == "1":
        card = input("Введите номер карты: ")
        result = get_mask_card_number(card)
    elif choice == "2":
        account = input("Введите номер счёта: ")
        result = get_mask_account(account)
    else:
        result = "Ошибка: неверный выбор. Введите 1 или 2."

    print("Результат маскировки:", result)


if __name__ == "__main__":
    mask_input()
