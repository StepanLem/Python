s = input()
count1 = 0
count0 = 0
for i in range(0, len(s)):
    if s[i] == '1':
        count1 += 1
    else:
        count0 += 1
if count0 == count1:
    print("yes")
else:
    print("no")
