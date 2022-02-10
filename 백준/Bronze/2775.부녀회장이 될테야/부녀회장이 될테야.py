T = int(input())
for i in range(T) :
  k = int(input())
  n = int(input())
  lst = [[]]
  for j in range(n) :
    lst[0].append(j+1)
  for j in range(k) :
    lst.append([])
    for l in range(n) :
      lst[j+1].append(sum(lst[j][:l+1]))
  
  print(lst[k][n-1])