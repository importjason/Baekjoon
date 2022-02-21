n = int(input())
lst = list(map(int, input().split()))
lst_ans = []

for i in range(1, len(lst)-1) :
  lst_ans.append(lst[i] + min(lst[i+1], lst[i-1]))

lst_ans.append(lst[0])
lst_ans.append(lst[-1])

print(max(lst_ans))
