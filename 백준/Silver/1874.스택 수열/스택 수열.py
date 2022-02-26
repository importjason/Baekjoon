from sys import stdin,stdout

n = int(input())
num_lst = []
stack = []
ans_lst = []
flag = 0

for i in range(n) :
  num_lst.append(int(stdin.readline().rstrip()))

num_add = 1

while num_lst :
  if num_add <= num_lst[0] :
    stack.append(num_add)
    num_add += 1
    ans_lst.append('+')
  elif stack[-1] == num_lst[0] :
    num_lst.pop(0)
    stack.pop(-1)
    ans_lst.append('-')
  else :
    print('NO')
    flag = 1
    break

if flag != 1 :
  for i in ans_lst :
    stdout.write(i+'\n')