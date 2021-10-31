from math import ceil
n,m=map(int, input().split())
al=list(map(int, input().split()))

if n==m:
    print(0)
    exit()

if m==0:
    print(1)
    exit()

al.sort()
al.append(n+1)

min_l = 10**18
prev = 0
for a in al:
    dist = a-prev-1
    if dist > 0:
        min_l = min(min_l, dist)
    prev = a

# print(min_l)

prev = 0
ans = 0
for a in al:
    dist = a-prev-1
    if dist > 0:
        ans += ceil(dist/min_l)
    prev = a
print(ans)