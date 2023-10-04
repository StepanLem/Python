s = input()
result = ""
for i in s:
    if i != " " and i != ")" and i != "(" and i != "-":
        result += i
print(result)
