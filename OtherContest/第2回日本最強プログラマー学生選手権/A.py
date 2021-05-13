x,y,z = map(int,input().split())

t = y/x

if t * z == int(t * z):
    s = t * z - 1
else:
    s = t * z

print(int(s))