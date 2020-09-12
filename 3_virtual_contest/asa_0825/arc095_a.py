n = int(input())
xl = list(map(int, input().split()))
xs = xl[:]
xs.sort()
med1 = xs[n//2-1]
med2 = xs[n//2]

for x in xl:
    if x <= med1:
        print(med2)
    else:
        print(med1)
