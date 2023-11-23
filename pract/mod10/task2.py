import re
import doctest


def is_valid_color(color):
    """
        Проверяет корректность пароля по критериям.
    :param color: запись цвета в одном из трёх web форматов.
    :type color: str
    :return: True, если запись цвета корректна, иначе False.
    :rtype: bool

    >>> is_valid_color('rgb(255, 255, 255)')
    True
    >>> is_valid_color('rgb(10%, 20%, 0%)')
    True
    >>> is_valid_color('rgb(257, 50, 10)')
    False
    >>> is_valid_color('#2345')
    False
    >>> is_valid_color('ffffff')
    False
    >>> is_valid_color('#21f48D')
    True
    >>> is_valid_color('#888')
    True
    >>> is_valid_color('hsl(200,100%,50%)')
    True
    >>> is_valid_color('hsl(34%, 20%, 50%)')
    False
    >>> is_valid_color('hsl(0, 0%, 0%)')
    True
    >>> is_valid_color('hsl(20, 10, 0.5)')
    False
    """
    rgb_pattern = re.compile(r'^rgb\((\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?), '
                             r'(\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?), '
                             r'(\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?)\)$')

    hex_pattern = re.compile(r'^#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})$')

    hsl_pattern = re.compile(r'^hsl\((\d{1,3}|[1-9]\d{0,2}),\s*(100%|[1-9]?\d%|0%),\s*(100%|[1-9]?\d%|0%)\)$')

    return bool(rgb_pattern.match(color) or hex_pattern.match(color) or hsl_pattern.match(color))


doctest.testmod()
