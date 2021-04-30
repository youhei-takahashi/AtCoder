from collections import deque

r,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
c = []
for i in range(r):
    c.append(input())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

dist = []   # 探索済かどうかと距離を格納
for i in range(r):
    dist.append( [-1] * C )
q = deque()
q.append([sy, sx])
dist[sy][sx] = 0    # 始点

while len(q) > 0:
    i, j = q.popleft()
    for i2, j2 in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:     # 上下左右を探索
        if not(0 <= i2 < r and 0 <= j2 < C):
            continue
        if c[i2][j2] == "#":
            continue
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1   # 壁や範囲外でなければ探索済みにする
            q.append([i2,j2])   # 新しい上下左右探索の対象としてキューに追加する

print(dist[gy][gx])