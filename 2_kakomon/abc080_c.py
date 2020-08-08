from itertools import product

n = int(input())
fl = []
for _ in range(n):
    row = list(map(int, input().split()))
    fl.append(row)

pl = []
for _ in range(n):
    row = list(map(int, input().split()))
    pl.append(row)

ite = product(range(2),repeat=10)
ans = -1*(10**9)
for it in ite:
    pattern = list(it)
    if 1 not in pattern: continue
    each_cnt = [0]*n
    for i,v in enumerate(pattern):
        if v == 1:
            for j,f in enumerate(fl):
                if f[i] == 1:
                    each_cnt[j] += 1
    val = 0
    for i, c in enumerate(each_cnt):
        val += pl[i][c]
    ans = max(ans,val)

print(ans)