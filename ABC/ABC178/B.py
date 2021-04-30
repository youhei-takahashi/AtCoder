li = list(map(int,input().split()))
 
a = li[0]
b = li[1]
c = li[2]
d = li[3]
 
 
ac = a * c
bc = b * c
ad = a * d
bd = b * d
result = ac
if result < bc:
    result = bc
if result < ad:
    result = ad
if result < bd:
    result = bd
if a <= 0 and 0 <= b and result < 0:
    result = 0
if c <= 0 and 0 <= d and result < 0:
    result = 0
print(result)