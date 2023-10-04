s = input()
symbol = ""
d = ""
space_count = 0
for i in range(0, len(s)):
  if s[i] != "," and space_count == 0:
    symbol += s[i]
  elif s[i] != "," and space_count == 1:
    d += s[i]
  else:
    space_count += 1
d = int(d)
print(chr(((ord(symbol) - 97) + d) % 26 + 97))
