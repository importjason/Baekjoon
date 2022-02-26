from sys import stdin,stdout

n = int(input())

lst_count = [0] * 10001

for i in range(n) :
  num = int(stdin.readline().rstrip())
  lst_count[num] += 1

for i in range(10001) :
  for j in range(lst_count[i]) :
    stdout.write(str(i)+'\n')