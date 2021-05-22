s = input()

s = s[::-1]

for x in s:
    if x == "6":
        print(9, end="")
    elif x == "9":
        print(6, end="")
    else:
        print(x, end="")
