import sys
import time

START_TIME = time.time()

N,M = map(int, input().split())

ma = [] # 探索済み
for _ in range(N):
    ma.append([False] * N)
for x in range(N):
    ma[x][x] = True
ans = N

li = []
for x in range(M):
    x, y = map(int, input().split())
    li.append([x-1,y-1])

if M == 0:
    print(N)
    sys.exit()


def dfs(i, x, y):
    global ans
    if not(ma[i][y]):
        ma[i][y] = True
        ans += 1
        for j,k in li:
            if j == y:
                dfs(i, j, k)

for i, j in li:
    dfs(i, i, j)
print(ans)

ELAPSED_TIME = time.time() - START_TIME
print('Elapsed Time:', ELAPSED_TIME*1000 ,'[ms]')