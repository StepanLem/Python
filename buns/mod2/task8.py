s, i = input().split(",")
count=0
for k in range(0,len(s)):
    if s[k]==i:
        count += 1
    else:
        break
print(count)