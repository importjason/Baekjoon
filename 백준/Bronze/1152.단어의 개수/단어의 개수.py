a = input()
b = a.strip()
if len(a) == 0 or a == ' ' :
    print(0)
else :
    print(1+b.count(' '))