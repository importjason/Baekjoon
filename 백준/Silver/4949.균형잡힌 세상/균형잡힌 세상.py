from sys import stdin

while True :
    line = stdin.readline().rstrip()
    lst = []

    if line == "." :
        break

    for i in line :
        if i == '[' or i == '(' :
            lst.append(i)
        elif i == ']' :
            if len(lst) != 0 and lst[-1] == '[' :
                lst.pop()
            else : 
                lst.append(']')
                break
        elif i == ')' :
            if len(lst) != 0 and lst[-1] == '(' :
                lst.pop()
            else :
                lst.append(')')
                break
    if len(lst) == 0 :
        print('yes')
    else :
        print('no')