from bisect import bisect_left, bisect_right

n,m=map(int, input().split())
al=list(map(int, input().split()))
al.sort()
ok, ng = 0, 10**18+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    # ...
    cnt=0
    for i,a in enumerate(al):
        need=mid-a
        ind = bisect_left(al, need)
        if ind==n: continue
        okcnt=(n-ind)
        cnt+=okcnt
    if cnt>=m: ok = mid
    else: ng = mid

csums=[0]
for a in al:
    csums.append(csums[-1]+a)

ans=0
rem=m
for i,a in enumerate(al):
    need=ok-a
    ind = bisect_right(al, need)
    if ind==n: continue
    okcnt=(n-ind)
    val=0
    val+=okcnt*a
    val+=csums[-1]-csums[ind]
    rem-=okcnt
    ans+=val

ans+=(rem*ok)
print(ans)