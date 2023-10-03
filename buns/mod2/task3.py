a, b, c = map(int, input().split())

max_num = max(a, b, c)
min_num = min(a, b, c)
middle_num = a + b + c - max_num - min_num

print(middle_num)
