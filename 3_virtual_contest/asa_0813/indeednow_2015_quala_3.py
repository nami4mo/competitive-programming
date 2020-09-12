from bisect import bisect_left, bisect_right

n = int(input())
sl = []
zero_cnt = 0
for _ in range(n):
    s = int(input())
    sl.append(s)
    if s == 0: zero_cnt+=1
sl.sort()


q = int(input())
ans = []
for _ in range(q):
    k = int(input())
    if n-zero_cnt <= k:
        ans.append(0)
        continue
    ok, ng = 10**6+1, -1
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        ok_flag = True
        # ...
        cnt = n - bisect_left(sl, mid)
        if cnt <= k:
            ok = mid
        else:
            ng = mid
    ans.append(ok)

for a in ans:print(a)