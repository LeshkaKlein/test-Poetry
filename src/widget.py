# Импортируем функции get_mask_card_number и get_mask_account из модуля masks.py
from src.masks import get_mask_card_number, get_mask_account

# Импорт модуля datetime
from datetime import datetime


def mask_account_card(info_user: str) -> str:
    """Функция обработки введенных данных Счет или Карта
    и вывода замаскированной информации"""

    if "Счет" in info_user:
        return get_mask_account(info_user)
    else:
        return get_mask_card_number(info_user)


def get_date(date_str: str) -> str:
    """Преобразует дату из ISO-формата (YYYY-MM-DDTHH:MM:SS[.ffffff]) в DD.MM.YYYY."""
    parsed_datetime = datetime.fromisoformat(date_str)
    return parsed_datetime.strftime("%d.%m.%Y")
