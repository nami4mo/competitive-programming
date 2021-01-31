a=input()
b=input()
n=len(a)
from collections import Counter
ca=Counter(a)
cb=Counter(b)

same=False
alps = 'abcdefghijklmnopqrstuvwxyz'
for c in alps:
    if ca[c]!=cb[c]:
        print('NO')
        exit()
    if ca[c]>=2: same=True

al=[]
bl=[]
cnt=0
for i in range(n):
    if a[i]!=b[i]:
        cnt+=1
        al.append(a[i])
        bl.append(b[i])

if cnt==0:
    if same:
        print('YES')
    else:
        print('NO')
    exit()

if cnt>6:
    print('NO')
    exit()

na=len(al)
swaps=[]
for i in range(na-1):
    for j in range(i+1,na):
        swaps.append((i,j))

from itertools import product
ite = list(product(swaps,repeat=3))
for pattern in ite:
    # print(pattern)
    aal=al[:]
    for u,v in pattern:
        aal[u],aal[v]=aal[v],aal[u]
        if same and aal==bl:
            print('YES')
            exit()
        # print(aal)
    if aal==bl:
        print('YES')
        exit()
print('NO')