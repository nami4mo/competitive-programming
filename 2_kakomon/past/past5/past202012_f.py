from itertools import product
n,m=map(int, input().split())
ml=[]
for _ in range(m):
    a,b,c=map(int, input().split())
    a-=1
    b-=1
    c-=1
    ml.append((a,b,c))

ans=0
ite = list(product(range(2),repeat=n))
for pattern in ite:
    usedl=set()
    cands=[]
    for i, v in enumerate(pattern):
        if v==1:usedl.add(i)
        else: cands.append(i)
    ok=True
    ansl=[False]*n
    for a,b,c in ml:
        cnt=0
        good=-1
        if a in usedl:cnt+=1
        else:good=a
        if b in usedl:cnt+=1
        else:good=b
        if c in usedl:cnt+=1
        else:good=c
        if cnt==3:
            ok=False
            break
        if cnt==2:
            ansl[good]=True
    cans=0
    for a in ansl:
        if a:cans+=1
    ans=max(ans,cans)
print(ans)
