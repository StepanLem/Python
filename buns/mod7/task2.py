import functools


def memoize(func):
    dictionary = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in dictionary:
            return dictionary[key]
        result = func(*args, **kwargs)
        dictionary[key] = result
        return result

    return wrapper


@memoize
def fibonacci(n):
    """
    Возвращает число Фибоначчи по индексу
    :param n:
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


func = fibonacci(7)
print(func)
print(f"Имя: {fibonacci.__name__}")
print(f"Документация: {fibonacci.__doc__}")
