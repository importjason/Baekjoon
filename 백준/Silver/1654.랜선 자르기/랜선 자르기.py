from sys import stdin

k,n = map(int, input().split())
lst = []

for _ in range(k) :
  lst.append(int(stdin.readline()))

beg = 1
end = max(lst)

while beg <= end :
  length = (beg + end) // 2
  piece = 0
  for i in lst :
    piece += i // length
  if piece >= n :
    beg = length + 1
  else :
    end = length - 1

print(end)