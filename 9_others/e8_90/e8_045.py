n,K=map(int, input().split())
xyl=[]
for _ in range(n):
    x,y=map(int, input().split())
    xyl.append((x,y))

max_ds=[0]*(1<<n)
for i in range(1<<n):
    cxyl=[]
    for j in range(n):
        if i&(1<<j):cxyl.append(xyl[j])
    l=len(cxyl)
    dmax=0
    for j in range(l):
        x0,y0=cxyl[j]
        for k in range(j+1,l):
            x1,y1=cxyl[k]
            d=(x1-x0)**2+(y1-y0)**2
            dmax=max(dmax,d)
    max_ds[i]=dmax
# print(max_ds)

ok, ng = 10**18+1,0
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    dp=[20]*(1<<n)
    dp[0]=1
    if max_ds[(1<<n)-1]<=mid:
        ok=mid
        continue
    
    for i in range(1<<n):
        if max_ds[i]<=mid:
            dp[i]=1
            continue
        bits=i
        val=20
        thre=i//2
        while bits>thre:
            bits=(bits-1)&i
            comp=bits^i
            v=dp[bits]+dp[comp]
            val=min(val,v)
        dp[i]=val
    if dp[(1<<n)-1]<=K: ok=mid
    else: ng=mid
print(ok)