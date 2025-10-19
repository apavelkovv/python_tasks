from typing import Callable, Iterable, Any

def filter_func(func: Callable[[Any], bool], string_arr: Iterable[Any]):
    """Фильтрует список строк по условию, заданному функцией func."""
    filtered_list = []
    for item in string_arr:
        if func(item):
            filtered_list.append(item)
    return filtered_list
