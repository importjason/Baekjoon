from sys import stdin
from collections import Counter

def banolim(n) :
  if n > 0 :
    if n % 1 >= 0.5 :
      return int(n + 0.5)
    else :
      return int(n)
  else :
    if n % -1 <= -0.5 :
      return int(n - 0.5)
    else :
      return int(n)

n = int(input())
lst = []

for i in range(n) :
  lst.append(int(stdin.readline().rstrip()))

lst.sort()

print(banolim(sum(lst) / n))  # 산술평균
print(lst[((n - 1) // 2)])  # 중앙값

mode = Counter(lst).most_common()
if len(mode) <= 2 :
  print(mode[0][0])
else :
  print(mode[1][0] if mode[0][1] == mode[1][1] else mode[0][0])  # 최빈값

print(max(lst) - min(lst))  # 범위