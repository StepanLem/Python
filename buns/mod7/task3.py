import functools
import time


def validate_args(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) < 1:
            return "Not enough arguments"
        if len(args) > 1:
            return "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"
        return func(*args, **kwargs)

    return wrapper


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


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        wrapper.execution_time = end_time - start_time
        # print(f"{func.__name__} выполнилась за {wrapper.execution_time:.6f} секунд")
        return result
    return wrapper


@timer
@validate_args
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@timer
@validate_args
@memoize
def fibonacci_memoized(n):
    if n <= 1:
        return n
    else:
        return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


result1 = fibonacci(30)
print(f"Время выполнения без memoize: {fibonacci.execution_time:.6f} секунд")

result2 = fibonacci_memoized(30)
print(f"Время выполнения с memoize: {fibonacci_memoized.execution_time:.6f} секунд")