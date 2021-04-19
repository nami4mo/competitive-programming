n=int(input())
al=list(map(int, input().split()))

from itertools import product
ite = list(product(range(2),repeat=n-1))
ans=10**18
for pattern in ite:
    xors=0
    val=0
    # flag=False
    for i, v in enumerate(pattern):
        a=al[i]
        val=val|a
        if v: 
            flag=True
            xors=xors^val
            val=0
        # else:
            # val=
    val=val|al[-1]
    xors=xors^val
    ans=min(ans,xors)
print(ans)