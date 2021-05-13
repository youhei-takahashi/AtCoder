n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
 
x = min(b) - max(a) + 1
if x > 0:
    print(x)
else:
    print(0)