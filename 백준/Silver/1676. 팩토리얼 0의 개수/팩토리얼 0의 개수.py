from math import factorial

n = int(input())
nfac = factorial(n)
lst = list(str(nfac))
lst = list(map(int,lst))

i = 0

while lst[-1] == 0 :
  lst.pop(-1)
  i += 1

print(i)