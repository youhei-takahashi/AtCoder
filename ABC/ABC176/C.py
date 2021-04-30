n = int(input())
li = list(map(int,input().split()))
 
ki = 0
s = 0
for i in range(0,n):
    if ki < li[i]:
        ki = li[i]
    else:
        s += ki-li[i]
print(s)