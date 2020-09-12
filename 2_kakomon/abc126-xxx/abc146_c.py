a,b,x = map(int, input().split())

ok, ng = 0,10**9+1
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    price = a*mid + b*len(str(mid))
    if price <= x:
        ok = mid
    else:
    	ng = mid
print(ok)