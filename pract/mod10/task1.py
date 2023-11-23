import re
import doctest


def check_password(password):
    """
    Проверяет корректность пароля по критериям.
    :param password: Строка-пароль для проверки.
    :type password: str
    :return: True, если пароль корректен, иначе False.
    :rtype: bool

    Examples:
    >>> check_password("rtG3FG!Tr^e")
    True
    >>> check_password("aA1!*!1Aa")
    True
    >>> check_password("oF^a1D@y5e6")
    True
    >>> check_password("enroi#$rkdeR#$092uWedchf34tguv394h")
    True
    >>> check_password("пароль")
    False
    >>> check_password("password")
    False
    >>> check_password("qwerty")
    False
    >>> check_password("lOngPa$$$W0Rd")
    False
    """
    is_valid_characters = bool(re.match("^[a-zA-Z0-9^$%@#&*!?]+$", password))
    is_length_valid = len(password) >= 6
    has_uppercase = len(re.findall("[A-Z]", password)) >= 2
    has_digit = len(re.findall("[0-9]", password)) >= 1
    has_special_chars = len(set(re.findall("[^a-zA-Z0-9]", password))) >= 2
    no_repeating_chars = not re.search(r"(.)\1\1", password)

    return (
        is_valid_characters and
        is_length_valid and
        has_uppercase and
        has_digit and
        has_special_chars and
        no_repeating_chars
    )


doctest.testmod()
