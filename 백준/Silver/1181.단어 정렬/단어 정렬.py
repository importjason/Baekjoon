import sys as sys

n = int(input())
arr = [[] for _ in range(51)]
for _ in range(n):
    temp = sys.stdin.readline().rstrip()
    arr[len(temp)].append(temp)
for i in range(1, len(arr)):
    arr[i].sort()
    back = ""
    for j in arr[i]:
        if back == j:
            continue
        print(j)
        back = j
