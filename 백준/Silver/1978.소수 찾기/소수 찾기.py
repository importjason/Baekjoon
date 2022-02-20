n = int(input())
lst = list(map(int,input().split()))
ans = 0

def pncheck(num) :    # 소수인지 확인하는 함수
  div = 0    # num의 약수의 개수
  for i in range(1, num+1) :
    if num % i == 0 :    # num을 1부터 num까지 하나씩 나눠보고, 약수 개수 확인
      div += 1
  if div == 2 :
    return(1)    # 약수의 개수 == 2 면 소수이므로 return(1)
  else :
    return(0)

for i in lst :
  ans += pncheck(i)    # lst의 숫자가 소수이면 ans에 1 추가, 아니면 0 추가. 결국 소수의 개수가 ans에 담긴다.

print(ans)
