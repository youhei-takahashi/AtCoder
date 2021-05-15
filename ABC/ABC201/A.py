
a,b,c = map(int,input().split())

if c -b  == b - a:
    print("Yes")
elif b - c == c - a:
    print("Yes")
elif c - a == a - b:
    print("Yes")
elif a - c == c - b:
    print("Yes")
elif a - b == b - c:
    print("Yes")
elif b - a == a - c:
    print("Yes")
else:
    print('No')