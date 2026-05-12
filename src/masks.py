def get_mask_card_number(card_number: int | str) -> str:
    """Маскирует номер банковской карты"""

    card_str = str(card_number)

    # Проверяем длину номера карты
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Форматируем номер карты
    masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return masked


def get_mask_account(account_number: int | str) -> str:
    """Маскирует номер банковского счета"""

    account_str = str(account_number)

    # Проверяем длину номера счета
    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    # Форматируем номер счета
    masked = f"**{account_str[-4:]}"
    return masked
