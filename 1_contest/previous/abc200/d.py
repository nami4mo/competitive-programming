n=int(input())
al=list(map(int, input().split()))

ds={}
from itertools import product
ite = list(product(range(2),repeat=min(8,n)))
for pattern in ite:
    bil=[]
    br=0
    for i, v in enumerate(pattern):
        if v==0:
            bil.append(i+1)
            br+=al[i]
    br%=200
    if br in ds:
        print('Yes')
        print(len(bil),*bil)
        print(len(ds[br]), *(ds[br]))
        exit()
    ds[br]=bil[:]

print('No')