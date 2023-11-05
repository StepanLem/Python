def armstrong_numbers_generator():
    num = 10
    while True:
        num_str = str(num)
        n = len(num_str)
        if num == sum(int(digit) ** n for digit in num_str):
            yield num
        num += 1


def get_armstrong_numbers():
    return next(armstrong_numbers_generator())


for i in range(8):
    print(get_armstrong_numbers(),  end=' ')
    