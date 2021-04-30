import itertools

n,m = map(int,input().split())
li = []
for i in range(0,n):
    li.append(list(map(int,input().split())))

ma = 0
for x in itertools.combinations(range(0,m),2):
    sum = 0
    for i in range(0,n):
        sum += max(li[i][x[0]],li[i][x[1]])
    if sum > ma:
        ma = sum
print(ma)