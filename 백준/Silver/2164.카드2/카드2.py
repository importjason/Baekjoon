from collections import deque
n = int(input())
q = deque()

for i in range(n) :
  q.append(i + 1)

while len(q) != 1 :
  del(q[0])
  q.rotate(-1)

print(q[0])