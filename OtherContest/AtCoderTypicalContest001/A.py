
# 深さ優先探索(DFS)の典型問題

import sys
sys.setrecursionlimit(1000000)

h,w = map(int, input().split())
m = []

# マップの読み込み
for _ in range(h):
    m.append(list(input()))

# スタートとゴールの位置検索
for x in range(h):
    for y in range(w):
        if m[x][y] == "s":
            si,sj = x,y
        if m[x][y] == "g":
            gi,gj = x,y

# 訪問済みフラグ
visited = []
for i in range(h):
    visited.append([False]*w)

def dfs(i, j):
    visited[i][j] = True

    for i2,j2 in [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]:
        if not (0 <= i2 < h and 0 <= j2 < w):   # 範囲外を無視
            continue
        if m[i2][j2] == "#":                    # 壁を無視
            continue
        if visited[i2][j2]:                     # 訪問済みを無視
            continue

        dfs(i2, j2)

# 始点から深さ優先探索を実行
dfs(si,sj)

if visited[gi][gj]:
    print("Yes")
else:
    print("No")