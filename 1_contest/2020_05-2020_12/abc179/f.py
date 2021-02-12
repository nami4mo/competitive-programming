from bisect import bisect_left, bisect_right

n,q = map(int, input().split())

hori_cnt = [n-2]*(n+2) # 2から

ql = []
for _ in range(q):
    c,x = map(int, input().split())
    ql.append((c,x))

tate_min = n
yoko_min = n
yoko_kyokai = []
ans1 = 0
for c,x in ql:
    if c == 1:
        if x < tate_min: 
            hori_cnt[yoko_min] = x-2
            yoko_kyokai.append(yoko_min*(-1))
            tate_min = x
    else:
        # print(c,x,'---------')
        if x < yoko_min:
            yoko_min = x
        # print(yoko_kyokai)
        ind = bisect_left(yoko_kyokai, x*(-1))-1
        # print(x,ind)
        if ind == -1:
            if x < yoko_min:
                ans1 += (tate_min-2)
            else:
                ans1 += (n-2)
            # print(tate_min-2,'++')
        else:
            val = yoko_kyokai[ind]
            ans1 += hori_cnt[val*(-1)]
            # print(hori_cnt[val*(-1)],'++s')


tate_cnt = [n-2]*(n+2) # 2から
yoko_min = n
tate_min = n
tate_kyokai = []
ans2 = 0
for c,x in ql:
    if c == 2:
        if x < yoko_min: 
            tate_cnt[tate_min] = x-2
            tate_kyokai.append(tate_min*(-1))
            yoko_min =x
            
    else:
        # print(c,x,'---------')

        if x < tate_min:
            tate_min = x

        ind = bisect_left(tate_kyokai, x*(-1))-1
        # print(tate_kyokai,'aaa')
        if ind == -1:
            if x < tate_min:
                ans2 += (yoko_min-2)
            else:
                ans2 += (n-2)
            # print(yoko_min-2,'+++')
        else:
            val = tate_kyokai[ind]
            ans2 += tate_cnt[val*(-1)]
            # print(tate_cnt[val*(-1)],'+++s')

print((n-2)*(n-2)-ans1-ans2)