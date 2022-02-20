from sys import stdin

n = int(stdin.readline())

lst = []

for i in range(n):
    cmd = stdin.readline().split()

    if cmd[0] == "push":
        lst.insert(0, cmd[1])

    elif cmd[0] == "pop":
        if len(lst) != 0:
          print(lst.pop())
        else:
          print(-1)

    elif cmd[0] == "size":
        print(len(lst))

    elif cmd[0] == "empty":
        if len(lst) == 0:
          print(1)
        else :
          print(0)

    elif cmd[0] == "front":
        if len(lst) == 0:
          print(-1)
        else:
          print(lst[len(lst) -1])

    elif cmd[0] == "back":
        if len(lst) == 0:
         print(-1)
        else:
          print(lst[0])