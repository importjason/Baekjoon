from sys import stdin
import math

casenum = int(input())

for i in range(casenum) :
  a,b = map(int,stdin.readline().split())
  print((a * b) // math.gcd(a,b))