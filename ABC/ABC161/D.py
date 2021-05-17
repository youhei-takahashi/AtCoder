
K = int(input())

li = []

def dfs(n):
    global li
    
    if n > 3234566667:  # テストケースより100000番目の値(KのMAX)
        return 
    li.append(n)
    x = n % 10
    if x > 0:
        dfs(10*n + x - 1)
    if 9 > x:
        dfs(10*n + x + 1)
    dfs(10*n + x)

for i in range(1,10):
    dfs(i)

li.sort()

# k番目を表示
print(li[K-1])