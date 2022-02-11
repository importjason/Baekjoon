T = int(input())
for i in range(T) :
  H, W, N = map(int, input().split())
  floor = str(N%H)
  room = str(N//H+1).zfill(2)
  if N%H == 0 :
    floor = str(H)
    room = str(N//H).zfill(2)
  print(floor+room)