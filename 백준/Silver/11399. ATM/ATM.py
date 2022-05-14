n = int(input())

lst = list(map(int,input().split()))
lst.sort()
ans = 0

for i in range(n) :
  ans += lst[i] * (len(lst)-i)

print(ans)