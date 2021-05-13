
n,k = map(int,input().split())
t = list(input())

for i in range(0,k-1):
    print(t[i],end="")
y = ord("Z")
for i in range(k-1,n):
    x = ord(t[i])
    if x > y:
        print(chr(x-32),end="")
    else:
        print(chr(x+32),end="")