from src.masks.masks import get_mask_account
from src.masks.masks import get_mask_card_number

__all__ = ["get_mask_card_number", "get_mask_account"]


def main() -> None:
    print("Banking app launched")
