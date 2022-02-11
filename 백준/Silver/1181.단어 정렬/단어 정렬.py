import sys
N = sys.stdin.readline().rstrip()

lst = []
for i in range(int(N)) :
    lst.append(sys.stdin.readline().rstrip())

lst = list(set(lst))   
lst.sort()
lst.sort(key=len)

for i in lst :
  print(i)