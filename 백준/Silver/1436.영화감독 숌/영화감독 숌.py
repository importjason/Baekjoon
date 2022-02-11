N = int(input())
num = 1
lst = []

while len(lst) != N :
  if str(num).count('666') > 0 :
    lst.append(num)
  num += 1

print(lst[-1])