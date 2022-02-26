from sys import stdin

n = int(input())
lst = []

for i in range(n) :
  num = int(stdin.readline().rstrip())
  if num == 0 :
    del lst[-1]
  else :
    lst.append(num)

print(sum(lst))