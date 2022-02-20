from sys import stdin

input = stdin.readline

lst = []

for i in range(int(input())) :
  co = list(input().rstrip().split())

  if co[0] == 'push' :
    lst.append(co[1])
  
  elif co[0] == 'pop' :
    if len(lst) == 0 :
      print(-1)
    else :
      print(lst.pop(-1))
  
  elif co[0] == 'size' :
    print(len(lst))

  elif co[0] == 'empty' :
    if len(lst) == 0 :
      print(1)
    else :
      print(0)

  elif co[0] == 'top' :
    if len(lst) == 0 :
      print(-1)
    else :
      print(lst[-1])