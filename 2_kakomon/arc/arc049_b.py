n=int(input())
xycl = []
for _ in range(n):
    x,y,c=map(int, input().split())
    xycl.append((x,y,c))

ng, ok = 0, 10**10
while abs(ok-ng) > 10**(-6):
    mid = (ok+ng)/2
    # print(mid)
    ok_flag = True
    # ...
    lx = -10**10
    rx = 10**10
    ly = -10**10
    ry = 10**10
    for x,y,c in xycl:
        d = mid/c
        lxx = x-d
        rxx = x+d
        lyy = y-d
        ryy = y+d
        lx = max(lx,lxx)
        rx = min(rx,rxx)
        ly = max(ly,lyy)
        ry = min(ry,ryy)
        if lx >= rx or ly >= ry:
            ok_flag = False
            break
    if ok_flag:
        ok = mid
    else:
    	ng = mid
print(ok)
