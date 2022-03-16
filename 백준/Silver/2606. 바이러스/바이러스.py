from sys import stdin

n = int(input())
m = int(input())

graph = [[] * n for _ in range(n+1)]

for _ in range(m):
  a,b = map(int, stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [0] * (n+1)
cnt = 0
def infected(num):
  global cnt
  visited[num] = 1
  for i in graph[num] :
    if visited[i] == 0 :
      visited[i] = 1
      infected(i)
      cnt += 1

infected(1)
print(cnt)