n,k = map(int, input().split())
al = list(map(int, input().split()))
fl = list(map(int, input().split()))
al.sort()
fl.sort(reverse=True)

ok, ng = 10**12+1, -1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    ok_flag = True
    # ...
    cnt = 0
    for a,f in zip(al,fl):
        v = a*f
        rem = a*f-mid
        cnt += max( (rem-1)//f+1, 0)
    if cnt <= k:
        ok = mid
    else:
    	ng = mid
print(ok)