L = int(input())
w = input()
a = 0

for i in range(L) :
  a += (ord(w[i])-96)*(31**i)

print(a % 1234567891)