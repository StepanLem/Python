def Row(a, n):
    if n==0: return 1
    if n%2==0:
        return Row(a*a,n/2)
    else:
        return a*Row(a,n-1)

print(Row(4,19))