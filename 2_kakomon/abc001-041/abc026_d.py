import math
a,b,c = map(int, input().split())

ok, ng = 1, 200
while abs(ok-ng) > 10**(-12):
    mid = (ok+ng)/2
    v = a*mid + b*math.sin(c*mid*math.pi)
    if v < 100.0:
        ok = mid
    else:
    	ng = mid
print(ok)