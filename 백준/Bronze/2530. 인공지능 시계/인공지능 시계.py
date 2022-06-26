a, b, c = map(int, input().split())
t = int(input())

cadd = t % 60
badd = (t % 3600) // 60
aadd = t // 3600

a += aadd
b += badd
c += cadd

if c >= 60 :
  b += c // 60
  c %= 60
  
if b >= 60 :
  a += b // 60
  b %= 60

if a >= 24 :
  a %= 24

print(a,b,c)