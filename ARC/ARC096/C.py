import sys

a,b,c,x,y = map(int,input().split())

mi = sys.maxsize

m = x if x > y else y
for i in range(0, m+1):
    sum = 2 * c * i
    if x > i:
        sum += (x - i) * a
    if y > i:
        sum += (y - i) * b
    if sum < mi:
        mi = sum
print(mi)