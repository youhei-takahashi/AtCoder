N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

cnt = [0] * N   # 0以上の場合はそのAは探索済み

for cc in c:
    cnt[b[cc-1]-1] += 1
s = 0
for aa in a:
    s += cnt[aa-1]

print(s)


