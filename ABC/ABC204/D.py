
N = int(input())
li = list(map(int,input().split()))

li.sort(reverse=True)

a,b = 0,0

for x in li:
    if a > b:
        b += x
    else:
        a += x
print(max(a,b))
