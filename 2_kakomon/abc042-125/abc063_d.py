n,a,b = map(int, input().split())
hl = []
for _ in range(n):
    hl.append(int(input()))

ok, ng = 10**9+1, 0
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    cnt = 0
    for h in hl:
        rem = h - b*mid
        if rem > 0:
            cnt += ( (rem-1)//(a-b) + 1 )
    if cnt <= mid:
        ok = mid
    else:
    	ng = mid
print(ok)
