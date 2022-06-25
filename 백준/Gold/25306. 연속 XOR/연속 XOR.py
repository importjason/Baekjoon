a,b = map(int,input().split())

def xorsum(a,b) :
  lsta = [a,a+1,a+2,a+3]
  lstb = [b-3,b-2,b-1,b]
  
  if a%4 == 0 :
    lsta = [0,0,0,0]
  
  if a%4 == 1 :
    lsta = [0,a,a+1,a+2]
  
  if a%4 == 2 :
    lsta = [0,0,a,a+1]
  
  if a%4 == 3 :
    lsta = [0,0,0,a]
  
  if b%4 == 0 :
    lstb = [b,0,0,0]
  
  if b%4 == 1 :
    lstb = [b-1,b,0,0]
  
  if b%4 == 2 :
    lstb = [b-2,b-1,b,0]
  
  if b%4 == 3 :
    lstb = [0,0,0,0]
  
  sum = 0
  for i in range(4) :
    sum ^= lsta[i]
    
  for i in range(4) :
    sum ^= lstb[i]
  
  return(sum)

print(xorsum(a,b))