from sys import stdin

n, price = map(int, input().split())

money_lst = []

for i in range(n):
    money_lst.append(int(stdin.readline().rstrip()))

money_lst.sort(reverse=True)

a = 0
ans = 0

while price != 0 :
  if price >= money_lst[a] :
    ans += price // money_lst[a]
    price = price % money_lst[a]

  else :
    a += 1

print(ans)