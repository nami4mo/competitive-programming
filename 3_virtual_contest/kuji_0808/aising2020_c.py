n = int(input())
ansl = [0]*(n+1)
for x in range(1,10**2+1):
    for y in range(1,10**2+1):
        for z in range(1,10**2+1):
            v = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if v <= n:
                ansl[v] += 1

for a in ansl[1:]:
    print(a)