import sys

while 1:
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        break

    idx = [False, False] + [True] * (n * 2 - 1)
    ans = 0

    for i in range(len(idx)):
        if idx[i]:
            for j in range(i * 2, 2 * n + 1, i):
                idx[j] = False

    for i in range(n + 1, 2 * n + 1):
        if idx[i]:
            ans += 1

    print(ans)