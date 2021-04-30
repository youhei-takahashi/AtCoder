x = list(map(int,input().split()))
a = x[0]
b = x[1]
c = x[2]
k = x[3]
 
if k < a + b:
    print(k)
else :
    print(a-(k-(a+b)))