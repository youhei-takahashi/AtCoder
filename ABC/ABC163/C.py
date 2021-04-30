n = int(input())
a = list(map(int,input().split()))
 
x = []
for i in range(0,n):
    x.append(0)
 
for i in a:
    x[i-1] += 1
 
for i in x:
    print(i)