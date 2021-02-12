n = int(input())

ansl = [0]*(n+1)

for x in range(1,10**2):
    for y in range(1, 10**2):
        for z in range(1,10**2):
            val = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if val <= n:
                ansl[val] += 1

for i in range(1,n+1):
    print(ansl[i])