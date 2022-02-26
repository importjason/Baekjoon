from sys import stdin

n,m = map(int, input().split())
lst = list(map(int,stdin.readline().split()))

beg = 0
end = max(lst)

while beg <= end :
  length = (beg + end) // 2
  takehome = 0
  for i in lst :
    if i > length :
      takehome += i - length
  if takehome >= m :
    beg = length + 1
  else :
    end = length - 1

print(end)