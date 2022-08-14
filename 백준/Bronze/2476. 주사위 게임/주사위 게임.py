from sys import stdin
casenum = int(input())
rwd_lst = []
for i in range(casenum) :
  a, b, c = map(int,stdin.readline().split())
  num_lst = [a,b,c]
  num_lst.sort()
  if a == b == c :
    rwd_lst.append(10000 + a * 1000)
  elif (num_lst[0] == num_lst[1]) or (num_lst[1] == num_lst[2]) :
    rwd_lst.append(1000 + num_lst[1] * 100)
  else :
    rwd_lst.append(max(num_lst) * 100)

print(max(rwd_lst))