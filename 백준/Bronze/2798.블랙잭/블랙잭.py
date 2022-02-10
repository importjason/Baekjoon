N, M = map(int, input().split())
lst = list(map(int, input().split()))
sum_lst = []
flag = 0
for i in range(N-2) :
  for j in range(i+1,N-1) :
    for k in range(j+1,N) :
      sum_lst.append(lst[i] + lst[j] + lst[k])

sum_lst.sort(reverse = True)

for i in sum_lst :
  if i <= M :
    print(i)
    break