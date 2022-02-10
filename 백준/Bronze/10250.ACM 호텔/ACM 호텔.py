import sys
n=int(sys.stdin.readline())
for x in range(n):
    h,w,n=map(int,sys.stdin.readline().split())
    floor = n%h #손님의 h위치 
    hosu = n//h+1 #손님의 w위치
    if n%h==0:
      hosu=n//h
      floor=h
    print("{}".format(floor*100+hosu))