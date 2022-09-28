casenum = int(input())
lst = []

for i in range(casenum) :
    lst.append(int(input()))

lst.sort()

for i in lst :
    print(i)