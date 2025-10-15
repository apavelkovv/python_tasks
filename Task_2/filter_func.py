def filter_func(func, string_arr):
    """Фильтрует список строк по условию, заданному функцией func."""
    filtered_list = []
    for item in string_arr:
        if func(item):
            filtered_list.append(item)
    return filtered_list
