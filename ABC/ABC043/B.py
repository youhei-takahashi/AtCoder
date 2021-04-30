s = input()
 
b = ""
for ss in s:
    if ss == "B":
        b = b[:-1]
    else:
        b += ss
print(b)