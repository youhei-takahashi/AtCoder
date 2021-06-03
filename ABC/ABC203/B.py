N,K = map(int,input().split())

sum = 0
for x in range(1, N+1):
    for y in range(1, K+1):
        sum += int(str(x) + "0" + str(y))
print(sum)