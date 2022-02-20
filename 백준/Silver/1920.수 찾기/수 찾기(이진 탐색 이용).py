from sys import stdin

def bsa(first, last, ans) :
  while first <= last :
    mid = (first + last) // 2
    if nlst[mid] == ans :
      return(1)
    elif nlst[mid] > ans :
      last = mid - 1
    else :
      first = mid + 1

  else :
    return(0)

n = int(input())
nlst = list(stdin.readline().split())
nlst.sort()

m = int(input())
mlst = list(stdin.readline().split())

for i in range(len(mlst)) :
  print(bsa(0, len(nlst) - 1, mlst[i]))
