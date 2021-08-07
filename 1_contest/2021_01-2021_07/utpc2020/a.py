n,l=map(int, input().split())
xal=[]
for _ in range(n):
    x,a=map(int, input().split())
    xal.append((x,a))

ok, ng = 10**18+1, -1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True

    t=mid
    prev_x=0
    for x,a in xal:
        t=min(mid, t+x-prev_x)
        t-=a
        if t<0:
            res=False
            break
        prev_x=x

    if res: ok = mid
    else: ng = mid
print(ok)