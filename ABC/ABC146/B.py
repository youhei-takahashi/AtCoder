n = int(input())
s = input()

for str in s:
    x = ord(str) + n
    if x >= 91:
        x -= 26
    print(chr(x),end="")