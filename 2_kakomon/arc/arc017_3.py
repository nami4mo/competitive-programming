from itertools import product
from bisect import bisect_left, bisect_right


n,x = map(int, input().split())
wl1 = []
wl2 = []
for i in range(n):
    if i < n//2:
        wl1.append(int(input()))
    else:
        wl2.append(int(input()))

wls1 = []
wls2 = []

n = len(wl1)
ite = list(product(range(2),repeat=n))
for pattern in ite:
    wsum = 0
    for i, v in enumerate(pattern):
        if v == 1: wsum += wl1[i]
    wls1.append(wsum)

 
n = len(wl2)
ite = list(product(range(2),repeat=n))
for pattern in ite:
    wsum = 0
    for i, v in enumerate(pattern):
        if v == 1: wsum += wl2[i]
    wls2.append(wsum)


wls1.sort()
wls2.sort()


ans = 0
for w in wls1:
    rem = x-w
    indl = bisect_left(wls2, rem)
    indr = bisect_right(wls2, rem) - 1
    cnt = max(0, indr-indl+1)
    ans += cnt

print(ans)