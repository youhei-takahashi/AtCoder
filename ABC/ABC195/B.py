import sys
a,b,w = map(int, input().split())
w *= 1000
 
c = 1
flg = True
while True:
    k = w / c
    if k <= b and k < a and flg:
        print("UNSATISFIABLE")
        sys.exit()
    if k <= b and flg:
        mi = c
        flg = False
    elif k < a:
        ma = c - 1
        break
    c += 1
print(mi, ma)