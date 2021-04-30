import math
 
li = list(map(int,input().split()))
n=li[0]
x=li[1]
t=li[2]
print( math.ceil(n/x)* t)