case = int(input())

def fibo(n) :
    
  zero_cnt = [0] * (n+2)
  one_cnt = [0] * (n+2)
  
  zero_cnt[0] = 1
  zero_cnt[1] = 0
  one_cnt[0] = 0
  one_cnt[1] = 1

  if n != 0 :
    for i in range(2,n+1) :
      zero_cnt[i] = zero_cnt[i-1] + zero_cnt[i-2]
      one_cnt[i] = one_cnt[i-1] + one_cnt[i-2]
    
    print(zero_cnt[n],one_cnt[n])

  else :
    print(1,0)

for i in range(case) :
  n = int(input())
  fibo(n)