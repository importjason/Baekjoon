A, B, V = map(int, input().split())
 
if (V - A) % (A - B) == 0:
    n = int((V - A)/(A - B))
else:
    n = int((V - A)/(A - B) + 1)
    
print(n + 1)