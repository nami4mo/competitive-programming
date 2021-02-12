n=int(input())

ok, ng = 0, 10**18+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    ok_flag = True
    # ...

    if mid*(mid+1)//2 <= n+1:
        ok_flag = True
    else:
        ok_flag = False

    if ok_flag:
        ok = mid
    else:
    	ng = mid
# print(ok)

print(n-ok+1)