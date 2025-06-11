from src.external_api.currency import convert_to_rub
from src.masks.masks import mask_account_number as get_mask_account
from src.masks.masks import mask_card_number as get_mask_card_number
from src.processing import filter_by_state
from src.processing import sort_by_date

__all__ = ["get_mask_account", "get_mask_card_number", "convert_to_rub", "filter_by_state", "sort_by_date"]


def init() -> None:
    """Initialize package components."""
    pass


def main() -> None:
    """Entry point for the banking application."""
    print("Banking app launched")


def generators() -> None:
    """Initialize generators module."""
    return None
