n,k,p=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
al.sort()
bl.sort()

bcl=[0]*(p+1)
for b in bl:
    bcl[b]+=1
for i in range(p):
    bcl[i+1]+=bcl[i]

# print(bcl)

def check_cnt(val):
    res=0
    for a in al:
        # cnt1 = bisect_right(bl, val-a)
        # # cnt2 = n - bisect_left(bl, p-a)
        # cnt2 = n - bisect_right(bl, p-a-1)
        # cnt3 = n - bisect_right(bl, val+p-a)
        # print(val-a, p-a-1)
        if val-a<0:
            cnt1=0
        else:
            cnt1=bcl[max(val-a,0)]
        cnt2=bcl[min(p,val+p-a)]-bcl[p-a-1]
        res+=(cnt1+cnt2)
    return res

ok, ng = 0, p
ok, ng = p-1, -1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    # ...
    cnt=check_cnt(mid)
    # print('---',mid,cnt)
    if cnt>=k: ok = mid
    else: ng = mid
print(ok)