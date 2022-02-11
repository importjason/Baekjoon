n = int(input())
ans = 99
def han(num) :
    nl = list(map(int,list(str(num))))
    if nl[2] - nl[1] == nl[1] - nl[0] :
        return True
if n < 100 :
    print(n)
else :
    for i in range(100,n+1) :
        if han(i) == True :
            ans += 1
    print(ans)