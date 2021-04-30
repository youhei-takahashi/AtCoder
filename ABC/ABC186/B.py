h,w = map(int, input().split())
 
li = list()
for _ in range(h):
    li.append(list(map(int,input().split())))
 
m = 101
for l in li:
    if min(l) < m:
        m = min(l)
 
result = 0
for l in li:
    result += sum(l) - m * w
 
print(result)