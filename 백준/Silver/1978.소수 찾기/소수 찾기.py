n = int(input())
lst = list(map(int,input().split()))
ans = 0

def pncheck(num) :
  div = 0
  for i in range(1, num+1) :
    if num % i == 0 :
      div += 1
  if div == 2 :
    return(1)
  else :
    return(0)

for i in lst :
  ans += pncheck(i)

print(ans)