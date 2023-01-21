casenum = int(input())
lst = list(map(int,input().split()))
n = int(input())
ans = 0
for i in lst :
    if i == n :
        ans += 1
print(ans)
        