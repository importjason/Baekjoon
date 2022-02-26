m,n = map(int, input().split())

array = [False] * 2 + [True] * (n - 1)

for i in range(2, n) :
    if array[i] == True :
        j = 2 
        while i * j <= n :
            array[i * j] = False
            j += 1

for i in range(m, n + 1) :
    if array[i] :
        print(i)