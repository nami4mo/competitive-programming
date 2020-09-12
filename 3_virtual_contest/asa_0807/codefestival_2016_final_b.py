n = int(input())

for i in range(10**6):
    v = i*(i-1)//2 + 1
    if v >= n:
        print