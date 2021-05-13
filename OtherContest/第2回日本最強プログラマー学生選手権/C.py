a,b = map(int, input().split())
for c in range(b, 0, -1):
    if b//c - (a-1)//c > 1:
        exit(print(c))