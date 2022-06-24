casenum = int(input())
for i in range(casenum) :
  n = int(input())
  if n == 1 :
    print(1)
    continue
  elif n == 2 :
    print(2)
    continue
  elif n == 3 :
    print(4)
    continue
  dp = [0] * (n+1)
  dp[1] = 1
  dp[2] = 2
  dp[3] = 4
  for j in range(4,n+1) :
    dp[j] = dp[j-1]+dp[j-2]+dp[j-3]
  print(dp[-1])