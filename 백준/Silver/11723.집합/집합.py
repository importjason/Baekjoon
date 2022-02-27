from sys import stdin,stdout

case =  int(input())
S = []

for i in range(case) :
  com = list(stdin.readline().split())

  if com[0] == 'add' and com[1] not in S :
    S.append(com[1])

  elif com[0] == 'remove' and com[1] in S :
    S.remove(com[1])

  elif com[0] == 'check' :
    if com[1] in S :
      stdout.write('1'+'\n')
    else :
      stdout.write('0'+'\n')

  elif com[0] == 'toggle' :
    if com[1] in S :
      S.remove(com[1])
    else :
      S.append(com[1])

  elif com[0] == 'all' :
    S = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
  elif com[0] == 'empty' :
    S = []