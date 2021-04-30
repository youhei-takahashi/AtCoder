li = list(map(int, input().split()))
 
if li.count(5) == 2 and li.count(7) == 1:
    print("YES")
else:
    print("NO")