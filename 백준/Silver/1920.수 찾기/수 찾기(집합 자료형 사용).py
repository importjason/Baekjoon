from sys import stdin, stdout
n = stdin.readline()
nlst = set(stdin.readline().split())
m = stdin.readline()
mlst = stdin.readline().split()

for i in mlst:
    print('1') if i in nlst else print('0')
