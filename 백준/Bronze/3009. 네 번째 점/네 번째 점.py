xlst = []
ylst = []
for i in range(3) :
  a,b = map(int,input().split())
  xlst.append(a)
  ylst.append(b)
print(min(xlst,key = lambda x : xlst.count(x)), min(ylst,key = lambda x : ylst.count(x)))