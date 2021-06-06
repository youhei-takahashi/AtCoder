
N = int(input())
A = list(map(int,input().split()))

sum = 0
for x in A:
    if x > 10:
        sum +=  x-10
print(sum)