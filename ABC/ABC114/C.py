import sys
sys.setrecursionlimit(1000000)

N = int(input())

ans = 0

def dfs(n, use3, use5, use7):
    global ans
    if n > N:   # 入力値を超えたらその枝はそこで探索終了
        return
    if use3 and use5 and use7:  # 3,5,7すべて含まれたらインクリメント
        ans += 1
    
    # 末尾にそれぞれの数字を付けて再帰
    dfs(n*10+3, True, use5, use7)
    dfs(n*10+5, use3, True, use7)
    dfs(n*10+7, use3, use5, True)


dfs(0, False, False, False)

print(ans)