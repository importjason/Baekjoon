from sys import stdin
from collections import deque

casenum = int(input())

for i in range(casenum) :
  n,m = map(int, input().split())
  imp_lst = list(map(int,stdin.readline().split()))
  imp_q = deque(imp_lst)
  idx_q = deque(imp_lst)
  idx_q[m] = 'target'
  ord = 0
  
  while True :
    if imp_q[0] == max(imp_q) :
      ord += 1
      if idx_q[0] == 'target' :
        print(ord)
        break
      else :
        imp_q.popleft()
        idx_q.popleft()
        
    else :
      imp_q.rotate(-1)
      idx_q.rotate(-1)