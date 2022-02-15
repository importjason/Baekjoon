a,b,c = map(int,input().split())
lst = [a,b,c]
p = 0
if a == b == c :
    p = 10000 + a * 1000
elif a == b or a == c :
    p = 1000 + a * 100
elif b == c :
    p = 1000 + b * 100
else :
    p = max(lst) * 100
print(p)