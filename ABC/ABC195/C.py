n = int(input())
 
x = len(str(n))
a = 3
sum = 0
while x > a:
    sum += n - int("9" * a)
    a += 3
 
print(sum)