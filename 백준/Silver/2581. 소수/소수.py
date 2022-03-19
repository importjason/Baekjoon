m = int(input())
n = int(input())

prime_lst = []
for num in range(m, n+1) :
  prime = 1
  if num > 1 :
    for i in range(2, num) :
      if num % i == 0 :
          prime = 0
          break
    if prime == 1 :
      prime_lst.append(num)
            
if prime_lst :
  print(sum(prime_lst))
  print(min(prime_lst))
else :
  print(-1)