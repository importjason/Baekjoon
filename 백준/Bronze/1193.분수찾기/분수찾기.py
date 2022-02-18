n = int(input())
minus = 1
while True :
  if n <= minus :
    break
  n -= minus
  minus += 1

if minus % 2 == 0 :
    print(n,'/',minus-n+1, sep = '')
else :
    print(minus-n+1,'/',n, sep = '')