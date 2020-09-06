from bisect import bisect_left, bisect_right

t=int(input())
for _ in range(t):
    n,k = map(int, input().split())
    xl = list(map(int, input().split()))
    yl = list(map(int, input().split()))
    xl.sort()
    left_cnts = []
    for i,x in enumerate(xl):
        rx = x+k
        ind_r = bisect_right(xl, rx) - 1
        cnt = ind_r-i+1
        left_cnts.append((cnt,ind_r))

    right_max_cnts = [-1]*n
    cmax = 0
    for i in range(n-1,-1,-1):
        x = xl[i]
        rx = x+k
        ind_r = bisect_right(xl, rx) - 1
        cnt = ind_r-i+1
        cmax = max(cmax,cnt)
        right_max_cnts[i] = cmax

    ans = 0
    for cnt, ind_r in left_cnts:
        if ind_r == n-1:
            ans = max(ans,cnt)
        else:
            v = cnt + right_max_cnts[ind_r+1]
            ans = max(ans,v)
    print(ans)