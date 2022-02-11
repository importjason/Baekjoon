n = input()
lst = [int(n) for n in input().split()]
lst = list(map(int,lst))
print(min(lst),max(lst))