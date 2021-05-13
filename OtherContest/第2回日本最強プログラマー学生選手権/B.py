n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = a + b
k = set(c)
for x in k:
    if c.count(x) == 1:
        print(x , end=" ")