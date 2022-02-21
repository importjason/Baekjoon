from sys import stdin

n = int(input())
lst = []
ranklst = []

for i in range(n):
  lst.append(list(map(int,stdin.readline().split())))

for i in range(n) :
  rank = 1
  for j in range(n) :
    if (lst[i][0] < lst[j][0]) and (lst[i][1] < lst[j][1]) :
      rank += 1
  ranklst.append(rank)

print(*ranklst, sep = ' ')