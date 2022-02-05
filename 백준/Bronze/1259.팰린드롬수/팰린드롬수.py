while True :
  a = input()
  if int(a) == 0 :
    break
  n = len(a)
  if ((n % 2 == 0) and (a[n//2-1::-1] == a[(n//2):])) :
    print('yes')
  elif (n % 2 == 1) and (a[(n-1)//2::-1] == a[(n-1)//2:]) :
    print('yes')
  else :
    print('no')