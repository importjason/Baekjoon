from sys import stdin,stdout

n, m = map(int, stdin.readline().split())
n_list = [stdin.readline().strip() for i in range(n)]
m_list = [stdin.readline().strip() for i in range(m)]

same = list(set(n_list) & set(m_list))

print(len(same))
for name in sorted(same):
    stdout.write(name+'\n')