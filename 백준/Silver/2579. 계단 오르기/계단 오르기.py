from sys import stdin

n = int(input())

s = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(n) :
  s[i+1] = int(stdin.readline().rstrip())



if n == 1 :
  print(s[1])
  
else :
  dp[1] = s[1]
  dp[2] = s[1] + s[2]
  
  for i in range(3,n+1) :
    dp[i] = max(dp[i-3] + s[i] + s[i-1], dp[i-2] + s[i])
  
  print(dp[n])