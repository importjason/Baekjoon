a = int(input())
lst = list(map(int, input().split()))
m = max(lst)
lst2 = [i/m*100 for i in lst]
print(sum(lst2)/a)