from collections import deque

h,w,n = map(int, input().split())
li = []
for i in range(h):
    s = input()
    li.append(s)
    if "S" in s:
        sh = i
        sw = s.find("S")

m = 0
for k in range(1, n+1):
    dist = []   # 探索済かどうかと距離を格納
    for i in range(h):
        dist.append( [-1] * w )
    dist[sh][sw] = 0        # スタートのコストを0に
    q = deque()
    q.append([sh,sw])

    while len(q) > 0:
        i,j = q.popleft()
        for i2,j2 in [[i-1,j], [i+1,j], [i,j-1], [i,j+1]]:
            if not( 0 <= i2 < h and 0 <= j2 < w):
                continue
            if li[i2][j2] == "X":
                continue
            if li[i2][j2] == str(k):
                sh = i2
                sw = j2
                m += dist[i][j] + 1
                # print(k,m)
                break
            if dist[i2][j2] == -1:
                dist[i2][j2] = dist[i][j] + 1
                q.append([i2,j2])
        else:
            continue
        break

print(m)