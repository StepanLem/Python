name = input("Введите имя файла: ") # "task5.txt"
try:
    with open(name, 'r') as file:
        s = file.read()
        dic = {}
        for letter in s:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1

        sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1]))

    with open("task5_result.txt", 'w') as file:
        for key, value in sorted_dic.items():
            file.write(f'{key}: {value}\n')
    print("Статистика успешно записана в файл.")
except FileNotFoundError:
    print("Файл не найден.")