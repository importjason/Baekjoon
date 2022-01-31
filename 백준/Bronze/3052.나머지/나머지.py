import sys
lst = []

for i in range(10) :
  a = int(sys.stdin.readline())%42
  if lst.count(a) == 0 :
    lst.append(a)

print(len(lst))