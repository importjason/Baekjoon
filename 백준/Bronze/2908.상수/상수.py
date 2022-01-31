a,b = map(list,input().split())

a.reverse()
b.reverse()

ja = ''.join(a)
jb = ''.join(b)

ia = int(ja)
ib = int(jb)

print(ia if ia > ib else ib)