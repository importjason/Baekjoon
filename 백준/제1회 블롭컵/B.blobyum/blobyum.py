from sys import stdin
input = stdin.readline

n,k = map(int, input().split())
lst = list(map(int, input().split()))

beg, end = 0, k - 1
thesum = sum(lst[beg:end+1])
sumlst = [thesum]

for i in range(n - 1):
  beg += 1
  if end + 1 < n :
    end += 1 
  else :
    end = (end + 1) % n
  thesum = thesum - lst[beg-1] + lst[end]
  sumlst.append(thesum)

print(max(sumlst))
