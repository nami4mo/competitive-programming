n,a,b = map(int, input().split())
hl = []
for _ in range(n):
    h = int(input())
    hl.append(h)


ok, ng = 10**10, 0
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    ok_flag = True
    cnt = 0
    for h in hl:
        rem = h - mid*b
        if rem > 0:
            need = (rem-1)//(a-b) + 1
        else:
            need = 0
        cnt += need
    # ...
    if cnt <= mid:
        ok = mid
    else:
    	ng = mid
print(ok)