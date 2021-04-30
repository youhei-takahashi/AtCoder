s = input()
t = input()
 
min = len(s)
for i in range(0,len(s)-len(t)+1):
    cnt = 0
    for j in range(0,len(t)):
        if s[i+j] != t[j]:
            cnt += 1
    if min > cnt :
        min = cnt
print(min)