a = int(input())
n = 1
for i in range(8) :
    b = int(input())
    if b > a :
        a = b
        n = i+2
print(a)
print(n)