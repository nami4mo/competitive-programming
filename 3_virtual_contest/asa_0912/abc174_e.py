# ng, ok = 0, 10**9+1

n,k = map(int, input().split())
al = list(map(int, input().split()))
ng, ok = 0, 10**9+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    ok_flag = True
    # ...
    cnt = 0
    for a in al:
        cnt += (a-1)//mid
    
    if cnt <= k:
        ok = mid
    else:
    	ng = mid
print(ok)

