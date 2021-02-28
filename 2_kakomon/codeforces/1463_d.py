import sys
input = sys.stdin.readline
ansl=[]
for _ in range(int(input())):
    n=int(input())
    bl=list(map(int, input().split()))
    bset=set(bl)
    rems=[]
    for i in range(1,2*n+1):
        if i not in bset: rems.append(i)
        
    ok, ng = 0,n+1
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        res = True
        for i in range(mid):
            if bl[i]>rems[n-mid+i]:
                res=False
                break
        if res: ok = mid
        else: ng = mid
    left_ok=min(ok,n)

    ok, ng = 0,n+1
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        res = True
        for i in range(mid):
            if bl[n-mid+i]<rems[i]:
                res=False
                break
        if res: ok = mid
        else: ng = mid
    right_ok=n-ok
    ans=left_ok-right_ok+1
    ans=max(0,ans)
    ansl.append(ans)

for a in ansl:print(a)