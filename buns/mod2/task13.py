s = input()
sum_odd = 0
sum_even = 0
for i in range(0, len(s)):
    if i % 2 != 0:
        sum_even += int(s[i])
    else:
        sum_odd += int(s[i])
if (sum_even * 3 + sum_odd) % 10 == 0:
    print("yes")
else:
    print("no")
