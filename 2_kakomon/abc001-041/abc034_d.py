n,k=map(int, input().split())
wpl=[]
for _ in range(n):
    w,p=map(int, input().split())
    wpl.append((w,p))


def check(mid):
    wppl=[]
    for w,p in wpl:
        val=w*(p-mid)
        wppl.append(val)
    wppl.sort(reverse=True)
    sums=sum(wppl[:k])
    return sums>=0


ok, ng = 0.0, 101.0
while abs(ok-ng) > 0.00001:
    mid = (ok+ng)/2
    ok_flag = check(mid)
    if ok_flag:
        ok = mid
    else:
    	ng = mid
print(ok)


