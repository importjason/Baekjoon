for i in range (int(input())) :
  lst = list(input())
  a = 0
  b = 0
  
  for i in range(len(lst)) :
    if lst[i] == 'O' :
      a += 1
      b += a
    else :
      a = 0
  
  print(b)