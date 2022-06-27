s = int(input())
i = 1
n = 0

while s - i >= 0 :
  s -= i
  n += 1
  i += 1

print(n)