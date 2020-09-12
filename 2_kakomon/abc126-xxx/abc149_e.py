from bisect import bisect_left, bisect_right

n,m = map(int, input().split())
al = list(map(int, input().split()))
al.sort()

ok, ng = 0, 10**18+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    ok_flag = True
    cnt = 0
    # print('-----')
    # print(ok,ng,mid)
    for i,a in enumerate(al):
        rem = mid-a
        cnt_a = n-bisect_left(al,rem)
        # cnt_a = min(n-i-1, cnt_a)
        cnt += cnt_a
        # print(i,a,cnt_a)
    if cnt >= m:
        ok = mid
    else:
    	ng = mid

min_sum = ok
cum_sums = [0]
csum = 0
for a in al:
    csum += a
    cum_sums.append(csum)
    
# print(min_sum)

ans = 0
cnt = 0
for i,a in enumerate(al):
    rem = min_sum - a
    ind = bisect_left(al, rem)
    # ind = ind if 0 <= ind < n else None
    # ind = max(i+1,ind)
    csum = cum_sums[n] - cum_sums[ind]
    # print(i,a,csum)
    ans += csum
    ans += a*(n-ind)
    cnt += (n-ind)

ans -= (cnt-m)*min_sum

print(ans)
# print(min_sum)