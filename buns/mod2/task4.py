decimal_number = int(input("Введите натуральное число в десятичной системе: "))

if decimal_number <= 0:
    print("Неверный ввод")
else:
    binary_representation = bin(decimal_number)[2:]
    octal_representation = oct(decimal_number)[2:]
    hexadecimal_representation = hex(decimal_number)[2:]
    print(f"{binary_representation}, {octal_representation}, {hexadecimal_representation}")