def Nod(a,b):
    if a == b:
        return a
    elif a > b:
        return Nod(a-b,b)
    else:
        return Nod(a,b-a)
print(Nod(int(input()),int(input())))