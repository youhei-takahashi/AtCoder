
n = int(input())

for i in range(30):
    if 1 + i * 100 <= n <= 100 + i * 100:
        print(i+1)
        break
