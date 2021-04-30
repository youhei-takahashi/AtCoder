n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = 0
a2 = 0
for i in range(n):
    a2 = max(a[i],a2)
    ma = a2 * b[i]
    if ma > m:
        m = ma
    print(m)