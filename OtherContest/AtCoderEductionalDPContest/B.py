# pypyじゃないとTLE

import sys

N,K = map(int,input().split())
h = list(map(int,input().split()))

cost = [sys.maxsize] * N

cost[0] = 0
cost[1] = abs(h[0]-h[1])

if N == 2:
    sys.exit(print(abs(h[0]-h[1])))

# まずはk以下の足場のコストを計算
for i in range(2, K):
    cost[i] = cost[0] + abs(h[0]-h[i])
    for j in range(1, K+1):
        if i - j < 0:
            continue
        m = cost[i-j] + abs(h[i-j]-h[i])
        if cost[i] > m:
            cost[i] = m
# k以降の足場のコストを計算
for i in range(K, N):
    for j in range(1, K+1):
        x = cost[i-j] + abs(h[i-j]-h[i])
        if cost[i] > x:
            cost[i] = x
print(cost[N-1])