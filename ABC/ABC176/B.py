n = input()
 
s = 0
for i in range(0,len(n)):
    s += int(n[i:i+1])
 
if s%9==0:
    print("Yes")
else:
    print("No")