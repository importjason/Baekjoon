from sys import stdin

price_given = int(input())

casenum = int(input())
price_sum = 0

for i in range(casenum) :
  a,b = map(int,input().split())
  price_sum += a*b

if price_sum == price_given :
  print("Yes")
else :
  print("No")