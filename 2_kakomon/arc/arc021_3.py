k=int(input())
n=int(input())
adl=[]
for _ in range(n):
    a,d=map(int, input().split())
    adl.append((a,d))

ng, ok = 0, 10**18+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    ok_flag = False
    # ...
    cnt = 0
    for a,d in adl:
        build_cnt = (mid-1-a)//d+1
        cnt += max(0,build_cnt)
    if cnt>=k:
        ok = mid
    else:
    	ng = mid

max_val = ok
cnt = 0
ans = 0
last_sums = []
for a,d in adl:
    build_cnt = (max_val-1-a)//d+1
    if build_cnt > 0:
        last_val = a+(build_cnt-1)*d
        valsum = build_cnt*(a+last_val)//2
        last_sums.append(last_val)
        cnt += build_cnt
        ans += valsum

last_sums.sort(reverse=True)
for i in range(cnt-k):
    ans -= last_sums[i]

print(ans)