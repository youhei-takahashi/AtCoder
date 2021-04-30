a,b = map(int, input().split())
 
if b == 1 and a == 1:
    print("Draw")
elif b == 1:
    print("Bob")
elif a == 1:
    print("Alice")
elif a < b:
    print("Bob")
elif b < a:
    print("Alice")
else :
    print("Draw")