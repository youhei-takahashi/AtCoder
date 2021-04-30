from collections import deque

w,h = map(int,input().split())
g = [[0]* (w+2)]
for _ in range(h):
    li= list(map(int,input().split()))
    li.insert(0, 0)
    li.append(0)
    g.append(li)
g.append([0]* (w+2))

dist = []
for _ in range(h+2):
    dist.append( [-1] * (w + 2) )

q = deque()
q.append([0, 0])
dist[0][0] = 0

cnt = 0
while len(q) > 0:
    i, j = q.popleft()
    li = [[i, j-1], [i,j + 1]]  # 左右
    if i % 2 == 0: # iが偶数の場合
        li.extend([[i-1,j-1], [i-1, j], [i+1, j-1], [i+1, j]])   #左上、右上、左下、右下のマス
    else:
        li.extend([[i-1,j], [i-1, j+1], [i+1, j], [i+1, j+1]])   #左上、右上、左下、右下のマス

    for i2, j2 in li:     # 隣接マスの探索
        if not(0 <= i2 < h+2 and 0 <= j2 < w+2):    # 範囲外
            continue
        if g[i2][j2] == 1:  # イルミネーション
            # dist[i][j] += 1
            cnt += 1
        if g[i2][j2] == 0:  # 建物なしの続き
            if dist[i2][j2] == -1: # 未探索であれば
                dist[i2][j2] = 0
                q.append([i2,j2])   # 新しい上下左右探索の対象としてキューに追加する

print(cnt)