s = input()
current_str = ""
for i in range (len(s)-1, -1, -1):
    if s[i] == ".":
        print(current_str[::-1])
        current_str = ""
    else:
        current_str += s[i]
print(current_str)
