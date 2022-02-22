from math import factorial
from sys import stdout

k,q = map(int, input().split())
lst = list(map(int, input().split()))

def checkblob(i,a,k) :
  while 1 :
    if (i * factorial(a)) % k == 0 :
      stdout.write(str(a) + ' ')
      break
    a += 1

for i in lst :
  a = 1
  checkblob(i,a,k)
