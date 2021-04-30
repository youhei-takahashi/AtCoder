w,h,n = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
li = [[1]*w for i in range(h)]
for t in data:
    x,y,a = t
    if a == 1:
        for i in range(h):
            li[i][:x] = [0] * x
    elif a == 2:
        for i in range(h):
            li[i][x:] = [0] * ( w - x )
    elif a == 3:
        for i in range(0,y):
            li[i] = [0] * w
    elif a == 4:
        for i in range(y,h):
            li[i] = [0] * w
result = 0
for l in li:
    result += sum(l)
print(result)