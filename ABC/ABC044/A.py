n = int(input())
k = int(input())
x = int(input())
y = int(input())
 
result = 0
if n < k:
    result += x * n
else :
    result += x * k
 
if n - k > 0:
    result += y * (n-k)