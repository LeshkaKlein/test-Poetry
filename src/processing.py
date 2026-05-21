def filter_by_state(my_list_dict: list, state: str = "EXECUTED") -> list:
    """Фильтрует список словарей, оставляя только записи с заданным статусом."""

    return [items for items in my_list_dict if items.get("state") == state]


def sort_by_date(my_list_dir: list, descending: bool = True) -> list:
    """Сортирует список словарей по дате (по умолчанию — от новых к старым)."""
    sorted_list = sorted(my_list_dir, key=lambda employee: employee["date"], reverse=descending)

    return sorted_list
