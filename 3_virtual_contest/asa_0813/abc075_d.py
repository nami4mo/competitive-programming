n,k = map(int, input().split())
xyl = []
for i in range(n):
    x,y = map(int, input().split())
    xyl.append((x,y))

ans = 10**20+1
for a in range(n):
    for b in range(a+1,n):
        axy = xyl[a]
        bxy = xyl[b]
        ax,ay = axy
        bx,by = bxy
        l = min(ax,bx)
        r = max(ax,bx)
        t = max(ay,by)
        bo = min(ay,by)
        v = 0
        for x,y in xyl:
            if l <= x <= r and bo <= y <= t:
                v += 1
        if v >= k:
            area = (r-l)*(t-bo)
            ans = min(ans, area)

        for c in range(b+1,n):
            cxy = xyl[c]
            cx,cy = cxy
            l = min(ax,bx,cx)
            r = max(ax,bx,cx)
            t = max(ay,by,cy)
            bo = min(ay,by,cy)
            v = 0
            for x,y in xyl:
                if l <= x <= r and bo <= y <= t:
                    v += 1
            if v >= k:
                area = (r-l)*(t-bo)
                ans = min(ans, area)

            for d in range(c+1,n):
                dxy = xyl[d]
                dx,dy = dxy
                left = min(ax,bx,cx,dx)
                right = max(ax,bx,cx,dx)
                top = max(ay,by,cy,dy)
                bottom = min(ay,by,cy,dy)
                cnt = 0
                for x,y in xyl:
                    if left <= x <= right and bottom <= y <= top:
                        cnt += 1
                if cnt >= k:
                    area = (right-left)*(top-bottom)
                    ans = min(ans, area)


print(ans)