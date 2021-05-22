
N = int(input())
H = list(map(int,input().split()))


cost = [0] * N  # n番目の足場までの最小コスト

cost[0] = 0     # 1つ目の足場

cost[1] = abs(H[0] - H[1])  # 2つ目の足場までのコスト

for i in range(2, N):
    cost[i] = min(cost[i-1] + abs(H[i-1]-H[i]), cost[i-2] + abs(H[i-2]-H[i]))

print(cost[N-1])