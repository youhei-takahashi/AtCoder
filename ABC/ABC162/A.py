n = int(input())
 
for i in range(0,3):
    if( n % 10 == 7):
        print("Yes")
        break
    n = int(n / 10)
else:
    print("No")