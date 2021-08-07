n,m=map(int, input().split())
abl=[]
for _ in range(m):
    a,b=map(int, input().split())
    abl.append((a-1,b-1))

k=int(input())
kl=[]
for _ in range(k):
    c,d=map(int, input().split())
    kl.append((c-1,d-1))

from itertools import product
ite = list(product(range(2),repeat=k))
ans=0
for pattern in ite:
    dishes=[False]*n
    for i, v in enumerate(pattern):
        dishes[kl[i][v]]=True
    cnt=0
    for a,b in abl:
        if dishes[a] and dishes[b]:
            cnt+=1
    ans=max(ans,cnt)

print(ans)