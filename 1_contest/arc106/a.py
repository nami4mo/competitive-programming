n = int(input())
for a in range(1,40):
    for b in range(1,30):
        if pow(3,a) + pow(5,b) == n:
            print(a,b)
            exit()

print(-1)