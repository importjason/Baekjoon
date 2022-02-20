from sys import stdin

n = int(input())

for i in range(n) :
  lst = list(stdin.readline().rstrip())
  br = 0    # 괄호가 열리면 br += 1 , 닫히면 br -= 1 을 한다. 
  for j in range(len(lst)) :
    if br < 0 :    # br이 음수가 되면 열리지 않은 괄호가 닫힌 것이므로 VPS가 될 수 없다
      break
    if lst[j] == '(' :
      br += 1
    else :
      br -= 1
  if br == 0 :    # 반복문이 종료되었을 때 br == 0 이면 모든 괄호가 정상적으로 닫혀 VPS 인것이고,
    print('YES')
  else :    # != 0 이면 괄호가 모두 정상적으로 닫히지 않은 것이므로 VPS가 아닌 것이다.
    print('NO')