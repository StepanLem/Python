i, n = input().split(",")
n = int(n)
print(chr(((ord(i) - 97) + n) % 26 + 97))