def filter_by_state(my_list_dict: list, state='EXECUTED') -> list:
    """
    Функция принимает список словарей и опционально значение для ключа state (по умолчанию
    'EXECUTED') и возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    """

    return [items for items in my_list_dict if items.get('state') == state]


def sort_by_date(my_list_dir: list, descending: bool = True) -> list:
    """
    Функция принимает список словарей и необязательный параметр, задающий
    порядок сортировки (по умолчанию — убывание) и возвращает новый список, отсортированный по
    дате (date).
    """
    sorted_list = sorted(my_list_dir, key=lambda employee: employee['date'], reverse=descending)

    return sorted_list


