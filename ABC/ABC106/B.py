n = int(input())
 
s = 0
for x in range(1,n+1, 2):
    cnt = 0
    for k in range(1,x+1):
        if x % k == 0:
            cnt += 1
    if cnt == 8:
        s += 1
print(s)