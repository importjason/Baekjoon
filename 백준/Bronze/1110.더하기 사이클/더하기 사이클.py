n = input()
if int(n) >= 10 :
  m = n[-1] + str(int(n[-1]) + int(n[-2]))[-1]
else :
  m = n[-1] + n[-1]
  
i = 1

while int(m) != int(n) :
  if int(m) >= 10 :
   m = m[-1] + str(int(m[-1]) + int(m[-2]))[-1]
  else :
   m = m[-1] + m[-1]

  i += 1

print(i)