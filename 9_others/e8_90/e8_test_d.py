n=int(input())
al=list(map(int, input().split()))

from itertools import product
ite = list(product(range(3),repeat=n))
for pattern in ite:
    bl=[0]*3
    for i, v in enumerate(pattern):
        bl[v]+=al[i]
    bl.sort()
    if bl[0]==bl[2]:
        print('Yes')
        exit()
print('No')