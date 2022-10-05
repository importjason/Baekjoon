X=int(input())
N=int(input())
flag = True
i = 0
sum=0
while flag :
  a,b=map(int, input().split())
  c = a*b
  sum+= c
  i += 1
  if i == N :
    flag = False
if X == sum:
  print('Yes')
else:
  print('No')