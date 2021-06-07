import sys
import time
sys.setrecursionlimit(10000)

N,M = map(int, input().split())

ma = [] # 探索済み配列
for _ in range(N):
    ma.append([False] * N)
ans = 0     # 解答

li = [[] for i in range(N)]     # 道データ
for x in range(M):
    x, y = map(int, input().split())
    li[x-1].append(y-1)

if M == 0:  # 道が無かったら
    print(N)
    sys.exit()

def dfs(i, j):   # 第1引数：起点、第2引数：移動先
    global ans
    if not(ma[i][j]):   # 既に移動済みでなければその先をさらに探索
        ma[i][j] = True
        ans += 1
        for k in li[j]:
            dfs(i, k)

for i in range(N):
    dfs(i, i)
print(ans)


