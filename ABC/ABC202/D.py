# 他人の提出コードを参考にしてAC

import itertools
from math import factorial

def comb_cnt(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))

A,B,K = map(int,input().split())

r = ""
while A > 0 and B > 0:
    m = comb_cnt(A-1+B, A-1)    # aを選んだ時の組合せの総数
    if K <= m:
        r += "a"
        A -= 1
    else:
        r += "b"
        B -= 1
        K -= m

r += "a"*A
r += "b"*B

print(r)


# for _ in range(0, A+B):
#     if 0 < a:
#         print("a,b",a,b)
#         m = int(factorial(a-1+b) / factorial(b) / factorial(a-1))
#         print("m:",m)
#         if K < m:
#             a -= 1
#             r += "a"
#         else :
#             b -= 1
#             r += "b"
#             K -= m
#     else:
#         r += "b"
#         b -= 1
    # if a == 1:
    #     r += "a"
    #     r += "b"*b
    #     break
    # # m = x + len(list(itertools.combinations(range(a-1+b), b))) # a始まりの組合せ
    # m = x + int(factorial(a-1+b) / factorial(b) / factorial(a-1))
    # print("m:" , m)
    # if K < m:
    #     a -= 1
    #     r += "a"
    # elif m == K:
    #     r += "b"*b
    #     r += "a"*a
    #     break
    # else:
    #     b -= 1
    #     r += "b"
    #     x += m





# x = list(range(0,A+1))
# x = list(itertools.combinations_with_replacement(x,B))
# x.reverse()

# s = "a" * A
# s = list(s)
# cnt = 0
# for i in x[K-1]:
#     s.insert(cnt+i,"b")
#     cnt+=1
# print("".join(s))

# s = "a" * (A+B)

# s = list(s)
# for i in x[K-1]:
#     s[i] = "b"
# print("".join(s))