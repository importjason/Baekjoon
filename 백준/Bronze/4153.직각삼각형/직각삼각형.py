while True :
  a, b, c = map(int, input().split())
  if (a and b and c) == 0 :
    break
  lst = [a, b, c]
  lst.sort()
  if lst[0]**2 + lst[1]**2 == lst[2]**2 :
      print('right')
  else :
      print('wrong')