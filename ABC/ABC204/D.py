import itertools
import sys
import math
sys.setrecursionlimit(10 ** 6)  # 再帰上限の引き上げ

N = int(input())
T = list(map(int,input().split()))

TMAX = sum(T)

dp = [[0] * (TMAX+1) for _ in range(N + 1)]
print(dp)
dp[0][0] = 1

# DP
for i in range(N):
    for j in range(TMAX + 1):
        if T[i] <= j:  # i+1番目の数字a[i]を足せるかも
            dp[i + 1][j] = dp[i][j - T[i]] or dp[i][j]
        else:  # 入る可能性はない
            dp[i + 1][j] = dp[i][j]
        print("i,j:",i,j)
        print(dp)

for j in range(math.ceil(TMAX/2), TMAX + 1):
    if 0 < dp[N][j]:
        print(j)
        exit()