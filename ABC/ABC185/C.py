L = int(input())
 
div = 1
for i in range(1,12):
    div *= i
 
div2 = 1
for i in range(1,12):
    div2 *= (L - i)
print(div2//div)