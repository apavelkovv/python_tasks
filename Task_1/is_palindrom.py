def is_palindrome(string: str) -> bool:
    """Проверяет, является ли строка палиндромом."""
    string = string.lower()
    string_reversed = string[::-1]
    return string_reversed == string
