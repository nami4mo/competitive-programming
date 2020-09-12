from bisect import bisect_left, bisect_right

n,k = map(int, input().split())
al = list(map(int, input().split()))
negal = []
posil = []
zero_cnt = 0
for a in al:
    if a > 0:
        posil.append(a)
    elif a == 0:
        zero_cnt += 1
    else:
        negal.append(abs(a))

negal.sort()
posil.sort()
nega_comb = len(negal)*len(posil)
zero_comb = zero_cnt*(zero_cnt-1)//2 + (len(negal)+len(posil))*zero_cnt

# ans = positive
if nega_comb+zero_comb < k:
    ng, ok = 0,10**18+1
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        cnt = nega_comb+zero_comb
        for i,nega in enumerate(negal):
            thre = mid//nega
            c_cnt = bisect_right(negal, thre)
            c_cnt -= (i+1)
            c_cnt = max(c_cnt,0)
            cnt += c_cnt
        for i,posi in enumerate(posil):
            thre = mid//posi
            c_cnt = bisect_right(posil, thre)
            c_cnt -= (i+1)
            c_cnt = max(c_cnt,0)
            cnt += c_cnt
        if k <= cnt:
            ok = mid
        else:
            ng = mid
    print(ok)

elif nega_comb < k:
    print(0)

# ans = negative
else:
    ng, ok = (10**18+1)*(-1), 0
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        cnt = 0
        for i,nega in enumerate(negal):
            thre = ((-1)*mid-1)//nega + 1
            c_cnt = len(posil) - bisect_left(posil, thre)
            cnt += c_cnt
        if k <= cnt:
            ok = mid
        else:
            ng = mid
    print(ok)