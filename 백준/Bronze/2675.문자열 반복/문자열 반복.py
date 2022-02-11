n = int(input())

for i in range(n):
    a, b = input().split()
    for ib in b:
        print(ib*int(a), end = '')
    print()