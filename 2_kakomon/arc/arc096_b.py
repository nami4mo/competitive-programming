from collections import deque

def solve(xcl,C,n):
    csums = []
    good_ps = []
    c_c = 0
    c_max = 0
    prev_x = 0
    for i in range(n):
        x,c = xcl[i]
        c_c -= (x-prev_x)
        prev_x = x
        c_c += c
        if c_c > c_max:
            good_ps.append(i)
            c_max = c_c
        csums.append(c_c)

    good_pq = deque(good_ps)
    dist = 0
    kal = 0
    ans = 0
    prev_x = 0
    for i in range(n-1,-1,-1):
        if good_pq and good_pq[-1] == i:
            good_pq.pop()

        # print('--',i)
        x,c = xcl[i]
        if i == n-1:
            dx = C-x
        else:
            dx = prev_x-x
        prev_x = x
        kal -= dx
        dist += dx
        kal += c
        ans = max(ans,kal)
        # print(kal)

        if good_pq:
            back_kal = kal-dist
            back_kal += csums[good_pq[-1]]
            ans = max(ans, back_kal)
            if good_pq[-1] == i:
                good_pq.pop()
        # print(good_pq)
        # print(ans)
    return ans


n,C = map(int, input().split())
xcl = []
for _ in range(n):
    x,c = map(int, input().split())
    xcl.append((x,c))


ans1 = solve(xcl,C,n)
xcl_r = []
for x,c in xcl[::-1]:
    xcl_r.append((C-x,c))

ans2 = solve(xcl_r,C,n)
ans = max(ans1,ans2)
print(ans)