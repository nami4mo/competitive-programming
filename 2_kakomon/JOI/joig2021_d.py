n,m,d=map(int, input().split())
xvl=[]
for _ in range(n):
    x,v=map(int, input().split())
    xvl.append((x,v))
xvl.sort()

ok=-1
ng=10**10
while abs(ok-ng)>1:
    mid=(ok+ng)//2
    px=-d
    cnt=0
    for x,v in xvl:
        if v<mid:continue
        if x-px<d:continue
        cnt+=1
        px=x
    if cnt>=m:ok=mid
    else:ng=mid
print(ok)