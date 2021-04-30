import sys
n,m,t = map(int,input().split())
z = n
now = 0
for i in range(0, m):
    a,b = map(int,input().split())
    z -= a - now
    if z <= 0:
        print("No")
        sys.exit()
    z += (b-a)
    if z > n:
        z = n
    now = b
z -= (t - now)
if z > 0:
    print("Yes")
else :
    print("No")
import sys
n,m,t = map(int,input().split())
z = n
now = 0
for i in range(0, m):
    a,b = map(int,input().split())
    z -= a - now
    if z <= 0:
        print("No")
        sys.exit()
    z += (b-a)
    if z > n:
        z = n
    now = b
z -= (t - now)
if z > 0:
    print("Yes")
else :
    print("No")
提出情報