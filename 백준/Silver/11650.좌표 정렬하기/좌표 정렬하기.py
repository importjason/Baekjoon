import sys

n = int(input())
lst = []
for i in range(n) :
  lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort()
for i in range(n) :
  print(*lst[i])