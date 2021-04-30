import math
 
n,d = list(map(int,input().split()))
 
# x = []
# y = []
cnt = 0
for i in range(0,n):
    x,y = list(map(int,input().split()))
    # x.append(a)
    # y.append(b)
    k = math.sqrt(x**2 + y**2)
    if k <= d :
        cnt += 1
 
print(cnt)