import itertools

A,B,K = map(int,input().split())

x = list(range(0,A+1))
x = list(itertools.combinations_with_replacement(x,B))
x.reverse()

s = "a" * A
s = list(s)
cnt = 0
for i in x[K-1]:
    s.insert(cnt+i,"b")
    cnt+=1
print("".join(s))
# s = "a" * (A+B)

# s = list(s)
# for i in x[K-1]:
#     s[i] = "b"
# print("".join(s))