# Импортируем функции get_mask_card_number и get_mask_account из модуля masks.py

from masks import get_mask_card_number, get_mask_account

def mask_account_card(info_user: str) -> str:
    """Функция обработки введенных данных Счет или Карта
    и вывода замаскированной информации"""

    if "Счет" in info_user:
        return get_mask_card_number(info_user)
    else:
        return get_mask_account(info_user)


# Импорт модуля datetime
from datetime import datetime

def get_date(date: str) -> str:
    """
    Функция преобразует дату в формат 'DD.MM.YYYY
    '"""
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date.strftime("%d.%m.%Y")


