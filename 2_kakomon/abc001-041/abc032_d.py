from collections import deque
from itertools import product

def solve1(n,w,vwl):
    l1=[]
    l2=[]
    n1=n//2
    n2=n-n1
    ite = list(product(range(2),repeat=n1))
    for pattern in ite:
        wsum=0
        vsum=0
        for i, v in enumerate(pattern):
            if v==1:
                v_,w_=vwl[i]
                wsum+=w_
                vsum+=v_
        l1.append((wsum,vsum))

    ite = list(product(range(2),repeat=n2))
    for pattern in ite:
        wsum=0
        vsum=0
        for i, v in enumerate(pattern):
            if v==1:
                v_,w_=vwl[i+n1]
                wsum+=w_
                vsum+=v_
        l2.append((wsum,vsum))

    l1.sort()
    l2.sort()
    vmax=0
    for i in range(len(l1)):
        vmax=max(vmax,l1[i][1])
        l1[i]=(l1[i][0],vmax)
    vmax=0
    for i in range(len(l2)):
        vmax=max(vmax,l2[i][1])
        l2[i]=(l2[i][0],vmax)
    
    q2=deque(l2[::-1])
    ans=0
    for w1,v1 in l1:
        if not q2:return ans
        while w1+q2[0][0]>w:
            q2.popleft()
            if not q2:return ans
        ans=max(ans,v1+q2[0][1])
    return ans


def solve2(n,w,vwl):
    vmax=1000*n
    dp=[[10**18]*(vmax+1) for _ in range(n+1)]
    dp[0][0]=0
    for i in range(n):
        vi,wi=vwl[i]
        for j in range(vmax+1):
            dp[i+1][j]=min(dp[i+1][j],dp[i][j])
            if j+vi<=vmax:
                dp[i+1][j+vi]=min(dp[i+1][j+vi], dp[i][j+vi], dp[i][j]+wi)
    for i in range(vmax,-1,-1):
        if dp[-1][i]<=w:
            return i


def solve3(n,w,vwl):
    wmax=min(w, 1000*n)
    dp=[[0]*(wmax+1) for _ in range(n+1)]
    for i in range(n):
        vi,wi=vwl[i]
        for j in range(wmax+1):
            dp[i+1][j]=max(dp[i+1][j],dp[i][j])
            if j+wi<=wmax:
                dp[i+1][j+wi]=max(dp[i+1][j+wi], dp[i][j+wi], dp[i][j]+vi)
    return max(dp[-1])


n,w=map(int, input().split())
vwl=[]
vmax=0
wmax=0
for _ in range(n):
    v_,w_=map(int, input().split())
    vwl.append((v_,w_))
    vmax=max(vmax,v_)
    wmax=max(wmax,w_)

if n<=30:
    ans=solve1(n,w,vwl)
elif vmax<=1000:
    ans=solve2(n,w,vwl)
else:
    ans=solve3(n,w,vwl)
print(ans)