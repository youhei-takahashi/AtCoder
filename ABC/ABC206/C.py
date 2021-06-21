# listだとTLEだったが、dictでACになった。

N = int(input())

A = list(map(int,input().split()))

x = {}

for i in A:
    if i in x.keys():
        x[i] += 1
    else:
        x[i] = 1

sum = 0
for z in x:
    sum += x[z] * (N - x[z])
print(sum//2)

# x = []
# y = []
# for i in A:
#     if i not in x:
#         x.append(i)
#         y.append(N-1)
#     else:
#         k = x.index(i)
#         y[k] -= 1

# sum = 0
# for z in y:
#     sum += z * (N - z)

# print(sum // 2)
