n = int(input())
 
x = n % 1000
if x != 0:
    print(1000 - n % 1000)
else:
    print(0)