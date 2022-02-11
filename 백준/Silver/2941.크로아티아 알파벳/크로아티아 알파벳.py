w = input()
ans = 0
lst = ['dz=','c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
for i in lst :
  n = w.count(i)
  w = w.replace(i,' ')
  ans += n

ans += len(w.replace(' ',''))

print(ans)