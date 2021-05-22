import sys
sys.setrecursionlimit(1000000)

N,Q = map(int,input().split())

val = [0] * N   # 頂点の値(初期値0)
flg = [False] * N   # 探索済みフラグ

ki = []     # 各頂点からの次の木
for _ in range(N):
    ki.append([])
for _ in range(N-1):
    x,y = map(int,input().split())
    ki[x-1].append(y-1)
    ki[y-1].append(x-1)

so = [0] * N     # カウンターを増やす各頂点ごとの操作(同一頂点に対する操作をまとめている)
for _ in range(Q):
    a,b = map(int,input().split())
    so[a-1] += b

# 頂点nの部分木すべてにxを加算
def dfs(n, p):
    if flg[n]:
        return
    flg[n] = True
    val[n] = so[n] + p
    for k in ki[n]:
        dfs(k, val[n])

val[0] = so[0]
flg[0] = True
for x in ki[0]:
    dfs(x, val[0])

# 出力
for x in val:
    print(x, end=" ")