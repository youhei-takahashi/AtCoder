import math
r,x,y = map(int,input().split())

# x,yまでの最短距離
m = math.sqrt((0-x)**2 + (0-y)**2)

if m < r:
    print(2)
else:
    print( math.ceil(m / r))