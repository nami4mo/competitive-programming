n=input()
l=len(n)

from itertools import product
ite = list(product(range(2),repeat=l))
ans=0
for pattern in ite:
    a=[]
    b=[]
    for i, v in enumerate(pattern):
        if v==0:a.append(n[i])
        else:b.append(n[i])
    if (not a) or (not b):continue
    a.sort(reverse=True)
    b.sort(reverse=True)
    a=''.join(a)
    b=''.join(b)
    a=int(a)
    b=int(b)
    val=a*b
    ans=max(ans,val)
print(ans)