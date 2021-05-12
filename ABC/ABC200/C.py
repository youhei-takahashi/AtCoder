

# X-Yが200の倍数である というのは　X % 200とY % 200が一致する　と言い換えられる
n = int(input())
a = list(map(int, input().split()))

a.sort()

dict = [[] for i in range(200)]     # 空の200個の配列を格納した配列(二次元配列)

for i in range(len(a)):
    dict[a[i]%200].append(i)

cnt = 0
for x in dict:
    k = len(x)
    if k >= 2:
        cnt += k * (k-1) // 2
print(cnt)


# 愚直に二重ループするとTLEする(当たり前)

# n = int(input())
# a = list(map(int, input().split()))

# a.sort()

# cnt = 0
# l = len(a)
# for i in range(0,l-1):
#     for j in range(i+1,l):
#         print(i,j)
#         if (a[i] - a[j]) % 200 == 0:
#             cnt += 1
# print(cnt)