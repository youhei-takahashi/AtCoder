s = input()
t = input()
 
if t.find(s) == 0 and len(s) + 1 == len(t):
    print("Yes")
else:
    print("No")