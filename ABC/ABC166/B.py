n,k = map(int, input().split())
 
sunuke_list = [0] * n
 
for _ in range(k):
    d = int(input())
    okasi_list = list(map(int, input().split()))
    for x in okasi_list:
        sunuke_list[x-1] += 1
 
cnt = 0
for y in sunuke_list:
    if y == 0:
        cnt += 1
print(cnt)