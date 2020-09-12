from math import ceil

n = int(input())
csfl = [tuple(map(int, input().split())) for _ in range(n-1)]

for i in range(n-1):
    c,s,f = csfl[i]
    t = s+c
    for j in range(i+1,n-1):
        c,s,f = csfl[j]
        if t <= s:
            t = s
        else:
            t = ceil(t/f)*f
        t += c
    print(t)

print(0)