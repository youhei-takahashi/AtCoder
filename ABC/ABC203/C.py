N,K = map(int,input().split())

li = []
for _ in range(N):
    li.append(list(map(int,input().split())))
k = K
li.sort()
for a,b in li:
    if a <= k:
        k += b
    else:
        break
print(k)
