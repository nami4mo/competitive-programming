from itertools import product
from math import gcd

a,b=map(int, input().split())
odds=[]
evens=[]
for i in range(a,b+1):
    if i%2==0:evens.append(i)
    else: odds.append(i)

primes=[2,3,5,7,11,13,17,19,23,29,31]

ans=0
ite = list(product(range(2),repeat=len(odds)))
for pattern in ite:
    avail={}
    for p in primes: avail[p]=True
    ok=True
    for i, v in enumerate(pattern):
        if v==1:
            for p in primes:
                if odds[i]%p==0:
                    if not avail[p]:
                        ok=False
                        break
                    else:
                        avail[p]=False
        if not ok:
            break
    else:
        ans+=1
        for even in evens:
            for p in primes:
                if (not avail[p]) and even%p==0:
                    break
            else:
                ans+=1
print(ans)