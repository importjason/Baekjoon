from sys import stdin

n,m,b = map(int, input().split())
lst = []
lst_ans = []
for _ in range(n) :
  lst.append(list(map(int, stdin.readline().split())))
  
maxheight = 0
mintime = 100000000

for i in range(min(map(min,lst)) , max(map(max,lst)) + 1) : # standard height
  hstack = 0
  hbreak = 0
  for j in range(n) :  # column
    for k in range(m) :  # row
      h = i - lst[j][k]
      if h > 0 :
        hstack += h
      elif h < 0 :
        hbreak -= h
  
  if hbreak + b < hstack :
    continue

  time = hbreak * 2 + hstack
  
  if time <= mintime :
    mintime = time
    maxheight = i

print(mintime, maxheight)