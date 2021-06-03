n=int(input())
lrs=[]
for _ in range(n):
    l,r=map(int, input().split())
    lrs.append((l,r))
lrs.sort()

lefts=[0]*(n+1)
leftslr=[(-1,-1)]*(n+1)
lmax=0
rmin=10**10
for i in range(n):
    l,r=lrs[i]
    lmax=l
    rmin=min(r,rmin)
    dist=rmin-lmax+1
    dist=max(0,dist)
    lefts[i+1]=dist
    leftslr[i+1]=(lmax,rmin)

rights=[0]*(n+1)
rightslr=[(-1,-1)]*(n+1)
lmax=0
rmin=10**10
for i in range(n):
    l,r=lrs[n-1-i]
    lmax=max(lmax,l)
    rmin=min(r,rmin)
    dist=rmin-lmax+1
    dist=max(0,dist)
    rights[i+1]=dist
    rightslr[i+1]=(lmax,rmin)


ans=0
for i in range(1,n):
    v=lefts[i]+rights[n-i]
    ans=max(ans,v)

for i in range(1,n-1):
    l,r=lrs[i]
    v1=r-l+1
    l1,r1=leftslr[i]
    l2,r2=rightslr[n-i-1]
    ll=max(l1,l2)
    rr=min(r1,r2)
    v2=max(0,rr-ll+1)
    ans=max(ans, v1+v2)
print(ans)