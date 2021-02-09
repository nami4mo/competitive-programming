n,m=map(int, input().split())
gl=[[False]*(n) for _ in range(n)]
half=(n+1)//2-1
l1=n//2
l2=n-l1
g1=[True]*(2**l1)
g2=[0]*(2**l2)
g12l=[[] for _ in range(l1)]
for _ in range(m):
    a,b=map(int, input().split())
    if a>b:a,b=b,a
    a-=1
    b-=1
    gl[a][b]=True
    gl[b][a]=True
    if a<l1 and b>=l1:
        g12l[a].append(b)

for i in range(2**l2):
    vl=[]
    for j in range(l2):
        if (i>>j)&1==1:vl.append(j)
    ok=True
    for a in range(len(vl)):
        for b in range(a+1,len(vl)):
            if gl[vl[a]+l1][vl[b]+l1]:
                ok=False
                break
        if not ok:break
    else:
        g2[i]=len(vl)

for j in range(l2):
    bit=(1<<j)
    for i in range(2**l2):
        if i&bit:
            p=g2[i]
            g2[i]=max(g2[i],g2[i^bit])

ans=0
for i in range(2**l1):
    vl=[]
    for j in range(l1):
        if (i>>j)&1==1:vl.append(j)
    ok=True
    for a in range(len(vl)):
        for b in range(a+1,len(vl)):
            if gl[vl[a]][vl[b]]:
                ok=False
                break
        if not ok:break
    if not ok: continue
    v2ok=[True]*(l2)
    for v in vl:
        # for j in range(l2):
            # if gl[v][j+l1]:v2ok[j]=False
        for v2 in g12l[v]:
            v2ok[v2-l1]=False

    v2bit=0
    for j in range(l2):
        if v2ok[j]:v2bit+=(1<<j)
    v2cnt=g2[v2bit]
    val=v2cnt+len(vl)
    ans=max(ans,val)
print(ans)