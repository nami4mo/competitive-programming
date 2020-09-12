from itertools import product
n,m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

abl = []
for a in al:
    arow = []
    for b in bl:
        ab = a&b
        arow.append(ab)
    abl.append(arow)

ite = list(product(range(2),repeat=9))
for orval, pattern in enumerate(ite):
    zeros = []
    for i, v in enumerate(pattern):
        if v == 0: zeros.append(9-i-1)
    cnt = 0
    for arow in abl:
        for ab in arow:
            for zero_i in zeros:
                if ab&(1<<zero_i) > 0:
                    break
            else:
                cnt += 1
                break
    if cnt == n:
        print(orval)
        break



    