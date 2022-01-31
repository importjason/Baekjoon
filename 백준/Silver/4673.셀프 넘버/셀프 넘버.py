num = list(range(10000))
def d(n) :
    return (sum(map(int,list(str(n)))) + n)

for i in range(10000) :
  if d(i) in num:
    num.remove(d(i))

print('\n'.join(map(str,num)))