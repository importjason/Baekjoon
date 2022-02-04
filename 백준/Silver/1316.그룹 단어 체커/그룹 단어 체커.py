n = int(input())
ans = n
for i in range(n) :
    w=input()
    for j in range(0,len(w)-1) :
        if (w[j] != w[j+1]) and (w[j] in w[j+1:]) :
            ans -= 1
            break
print(ans)