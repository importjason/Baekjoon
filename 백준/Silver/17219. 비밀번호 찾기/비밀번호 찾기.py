from sys import stdin,stdout

n,m = map(int, stdin.readline().split())
n_dic = {}

for i in range(n) :
  a,b = stdin.readline().split()
  n_dic[a] = b

for i in range(m) :
    stdout.write(n_dic[stdin.readline().rstrip()]+'\n')