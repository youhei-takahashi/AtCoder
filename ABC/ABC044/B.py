import string
w = input()
 
letters = "abcdefghijklmnopqrstuvwxyz"
for ch in letters:
    if w.count(ch) % 2 != 0:
        print("No")
        break
else:
    print("Yes")