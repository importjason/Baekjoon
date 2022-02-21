from collections import deque
from sys import stdin

def sumthelist(lst, num) :
  sum = 0
  for i in range(num):
    sum += lst[i]
  return sum

q = deque()

n,k = map(int,input().split())

q = deque(list(map(int, stdin.readline().split())))

sumlst = []

for i in range(n):
  sumlst.append(sumthelist(q,k))
  q.rotate(1)

print(sumlst)
print(max(sumlst))
