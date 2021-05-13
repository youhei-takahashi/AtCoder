n = input()

for i in range(0,len(n)+1):
    n2 = "0" * i + n
    if n2 == n2[::-1]:
        print("Yes")
        break
else:
    print("No")