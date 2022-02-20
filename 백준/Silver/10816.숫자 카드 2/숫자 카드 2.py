from collections import Counter
from sys import stdin

n = stdin.readline().rstrip()
lst_n = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
lst_m = list(map(int,stdin.readline().split()))

dic_c = Counter(lst_n)

for i in range(len(lst_m)):
    if lst_m[i] in dic_c:
        print(dic_c[lst_m[i]], end=' ')
    else:
        print(0, end=' ')