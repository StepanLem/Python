import functools


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


@validate_args
def do(x):
    return f"{x}"


print(do(8))
print(do())
print(do(1, 2))
print(do(str(8)))
print(do(-2))

