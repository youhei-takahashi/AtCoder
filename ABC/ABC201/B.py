
n = int(input())

height = []
yama = []
for _ in range(n):
    y,h = input().split()
    yama.append(y)
    height.append(int(h))
newy = sorted(height, reverse=True)
print(yama[height.index(newy[1])])
