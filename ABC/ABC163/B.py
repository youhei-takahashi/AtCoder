n,m = map(int,input().split())
a = list(map(int,input().split()))
 
for i in range(0,m):
    n -= a[i]
 
if(n < 0):
    print(-1)
else:
    print(n)