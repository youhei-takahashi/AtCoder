n,k = map(int, input().split())
 
r = k
for _ in range(n-1):
    r *= k-1
print(r)