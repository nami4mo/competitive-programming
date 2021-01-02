n,m,k=map(int, input().split())
hl=list(map(int, input().split()))
cl=list(map(int, input().split()))

hil=[]
for i in range(n):
    hil.append((hl[i],i))
hil.sort()
i2hi=[-1]*n # use this
hi2i=[-1]*n # back to orig at last
for i in range(n):
    _, orig_i = hil[i]
    i2hi[orig_i]=i
    hi2i[i]=orig_i

# print(i2hi)
gl=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    aa=i2hi[a]
    bb=i2hi[b]
    if aa<bb:
        gl[bb].append(aa)
    else:
        gl[aa].append(bb)

INF=10**10
dp=[INF]*n
for c in cl:
    dp[i2hi[c-1]]=0
# print(i2hi)
# print(hi2i)
# print(dp)
for i in range(n):
    if dp[i]==0:continue
    ans=INF
    for neib in gl[i]:
        ans=min(ans,dp[neib]+1)
    dp[i]=ans

ansl=[-1]*n
for i in range(n):
    ansl[hi2i[i]]=dp[i]
    if ansl[hi2i[i]]>=INF: ansl[hi2i[i]]=-1

for a in ansl:print(a)