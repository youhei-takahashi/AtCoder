import sys

N,L = map(int,input().split())

x = list(map(int,input().split()))
T1, T2, T3 = map(int, input().split())

# ハードルがある座標はTrueとなるリスト
H = [False] * (L + 1)
for k in x:
    H[k] = True

# 各座標への最小移動コスト
cost = [10**100] * (L + 1)

cost[0] = 0

for i in range(1, L+1):
    # 行動1
    cost[i] = min(cost[i], cost[i-1] + T1)

    # 行動2
    if i > 1:
        cost[i] = min(cost[i], cost[i-2] + T1 + T2)

    # 行動3
    if i > 3:
        cost[i] = min(cost[i], cost[i-4] + T1 + T2 * 3)

    if H[i]:
        cost[i] += T3

cost[L] = min(cost[L], cost[L-3] + T2 * 2 + T2//2 + T1//2,
                cost[L-2] + T2 + T2//2 + T1//2,
                cost[L-1] + T2//2 + T1//2)

print(cost[L])
