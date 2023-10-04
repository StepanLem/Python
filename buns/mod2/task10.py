s = input()
result = ""
for i in range(0, len(s)):
    if s[i] == " ":
        result += s[i - 1]
    elif i == len(s) - 1:
        result += s[i]
    else:
        continue
print(result)
