n,k = map(int, input().split())
al = list(map(int, input().split()))

ok, ng = 10**9+1, 0
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    # mid = (ok+ng) / 2
    cnt = 0
    for a in al:
        a_cnt = (a-1)//mid
        cnt += max(0,a_cnt)

    if cnt <= k:
        ok = mid
    else:
    	ng = mid

print(ok)