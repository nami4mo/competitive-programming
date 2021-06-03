t,n=map(int, input().split())

ok, ng = 0, 10**18
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    # ...
    start=1*(100+t)//100
    end=mid*(100+t)//100
    taxc=end-start+1
    notaxc=mid
    cnt=taxc-notaxc
    # print(mid,start,end,notaxc,cnt)
    if cnt>=n:
        res=False
    else:
        res=True
    if res: ok = mid
    else: ng = mid
# print(ok)
ans=ok*(100+t)//100+1
print(ans)