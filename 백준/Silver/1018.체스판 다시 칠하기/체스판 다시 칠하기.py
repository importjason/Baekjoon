import sys

n,m = map(int, input().split())
lst = []
lst_ans = []

for i in range(n) :
  lst.append(list(sys.stdin.readline().rstrip()))

for a in range(n-7) :
  for b in range(m-7) :
    ans1 = 0
    ans2 = 0
    for i in range (a,a+8) :
      for j in range (b,b+8) :
       if (((i+j) % 2 == 0) and (lst[i][j] != 'W')) or (((i+j) % 2 == 1) and (lst[i][j] != 'B')) :
         ans1 += 1
       if (((i+j) % 2 == 1) and (lst[i][j] != 'W')) or (((i+j) % 2 == 0) and (lst[i][j] != 'B')) :
         ans2 += 1
    lst_ans.append(min(ans1,ans2))

print(min(lst_ans))