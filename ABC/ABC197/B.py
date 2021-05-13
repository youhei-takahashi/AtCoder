import sys

h,w,x,y = map(int, input().split())
m = []
for k in range(h):
    s = input()
    m.append(list(s))
x -= 1
y -= 1
cnt = 1
if m[x][y] == "#":
    print(0)
    sys.exit()
# 右へ
for i in range(y+1,w):
    # print(x,i,end="")
    # print(m[x][i])
    if m[x][i] == "#":
        break
    cnt += 1
# 左へ
yy = y - 1
while 0 <= yy:
    # print(m[x][yy])
    if m[x][yy] == "#":
        break 
    cnt += 1
    yy -= 1
# 下へ
for i in range(x+1,h):
    # print(i,y,end="")
    # print(m[i][y])
    if m[i][y] == "#":
        break
    cnt += 1
# 上へ
xx = x - 1
while 0 <= xx:
    # print(m[xx][y])
    if m[xx][y] == "#":
        break 
    cnt += 1
    xx -= 1
print(cnt)