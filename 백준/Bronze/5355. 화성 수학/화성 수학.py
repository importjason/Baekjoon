from sys import stdin

casenum = int(input())

for i in range(casenum) :
  lst = list(stdin.readline().split())
  n = float(lst[0])
  for i in lst :
    if i == '@' :
      n *= 3
    if i == '%' :
      n += 5
    if i == '#' :
      n -= 7

  print(f'{n:.2f}')