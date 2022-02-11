a = int(input())
flag = 1
def hap(n) :
  N = [int(j) for j in n]
  return int(n) + sum(N)

for i in range(1000000) :
  i = str(i)
  if hap(i) == a :
    print(i)
    flag = 0
    break

if flag == 1 :
  print(0)