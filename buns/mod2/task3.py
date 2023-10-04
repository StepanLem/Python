s = input()
a = ""
b = ""
c = ""
space_count = 0
for i in range(0, len(s)):
    if s[i] != " " and space_count == 0:
        a += s[i]
    elif s[i] != " " and space_count == 1:
        b += s[i]
    elif s[i] != " " and space_count == 2:
        c += s[i]
    else:
        space_count += 1
a = int(a)
b = int(b)
c = int(c)
if a > b:
    if b > c:
        print(b)
    elif a > c:
        print(c)
    else:
        print(a)
elif a > c:
    print(a)
elif b > c:
    print(c)
else:
    print(b)
