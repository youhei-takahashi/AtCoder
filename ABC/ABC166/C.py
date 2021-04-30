n,m = map(int, input().split())
 
h_list = list(map(int, input().split()))
result_list = [1] * n
for _ in range(m):
    x,y = map(int, input().split())
    if h_list[x-1] == h_list[y-1]:
        result_list[x-1] = 0
        result_list[y-1] = 0
    elif h_list[x-1] > h_list[y-1]:
        result_list[y-1] = 0
    else:
        result_list[x-1] = 0
# print(result_list)
print(sum(result_list))