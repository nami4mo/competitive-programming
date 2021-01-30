from heapq import heapify, heappop, heappush

n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))

asum=sum(al)
bsum=sum(bl)

bq=[]
for i in range(n):
    b=bl[i]
    heappush(bq,(-b,i))

ans=0
while bq:
    b,i1=heappop(bq)
    b*=-1
    i0=i1-1
    i2=i1+1
    if i0==-1:i0=n-1
    if i2==n: i2=0

    ac=bl[i0]+bl[i2]
    if b==al[i1]:continue
    if ac>=b:continue
    if b-ac<al[i1]:break

    cnt=(b-al[i1])//ac
    ans+=cnt
    bl[i1]-=ac*cnt
    bsum-=ac*cnt
    if bl[i1]!=al[i1]:
        heappush(bq,(bl[i1]*(-1),i1))
    if asum==bsum:break

if al==bl:
    print(ans)
else:
    print(-1)
