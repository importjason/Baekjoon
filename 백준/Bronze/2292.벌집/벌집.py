n = int(input()) - 2
i = 1

if n == -1 :
  print(1)

else :
  while True :
    n -= 6 * i
    if n < 0 :
        print(i+1)
        break
    i = i + 1