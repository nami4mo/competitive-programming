n=int(input())

from itertools import product
ite = list(product(['(',')'],repeat=n))
for pattern in ite:
    l=0
    for i, v in enumerate(pattern):
        if v=='(':l+=1
        else:l-=1
        if l<0:break
    else:
        if l==0:
            print(''.join(list(pattern)))