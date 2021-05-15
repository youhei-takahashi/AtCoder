
import itertools

s = list(input())
li = []
tli = []
for i in range(10):
    if s[i] == "o":
        li.append(i)
        tli.append(i)
    elif s[i] == "?":
        li.append(i)
cnt = 0
for x in itertools.product(li,li,li,li):
    flg = True
    for k in tli:
        if k not in x:
            flg = False
            break
    if flg:
        cnt += 1

print(cnt)

# import collections


# c = collections.Counter(list(input()))

# o = c["o"]
# x = c["x"]
# q = c["?"]


# if o > 4:
#     print(0)
# elif o == 4:
#     print(24)
# elif o == 3:


# if count()


