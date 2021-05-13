n = int(input())
s = input()
q = int(input())
li = list(s)

flg = False
for _ in range(q):
    t,a,b = list(map(int,input().split()))
    a -= 1
    b -= 1
    if t == 1:
        if flg:
            aa = a + n if a < n else a - n
            bb = b + n if b <    n else b - n
            li[aa],li[bb] = li[bb],li[aa]       # aa番目とbb番目の文字を入替え
        else:
            li[a],li[b] = li[b],li[a]
    else:
        flg = not flg

if flg:
    for i in range(n,len(li)):
        print(li[i],end="")
    for i in range(0,n):
        print(li[i],end="")
else:
    for x in li:
        print(x,end="")

# TLEするコード(問題文の通りに実施している)

# n = int(input())
# s = input()
# q = int(input())
# li = list(range(0,2*n))

# for _ in range(q):
#     t,a,b = list(map(int,input().split()))
#     if t == 1:
#         tmp = li[a-1]
#         li[a-1] = li[b-1]
#         li[b-1] = tmp
#     else:
#         li = li[n:] + li[:n]

# for x in li:
#     print(s[x],end="")