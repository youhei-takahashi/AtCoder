n,l = map(int, input().split())
 
li = []
for i in range(n):
    li.append(input())
 
li = sorted(li)
 
for s in li:
    print(s, end="")