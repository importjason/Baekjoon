import sys

for i in range(int(input())) :
    lst = list(map(int,sys.stdin.readline().split()))
    n = lst[0]
    del lst[0]
    m = sum(lst)/n
    s = 0
    for i in range(n) :
        if lst[i]>m :
            s += 1
    print(format(s/n*100,'.3f'),'%',sep='')