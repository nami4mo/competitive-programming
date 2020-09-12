n,k = map(int, input().split())
ans = 0
abl = [ tuple(map(int, input().split())) for _ in range(n) ]

kset = set()
kset.add(k)
for i in range(30):
    if k&(1<<i) == 0: continue
    v = 0
    for j in range(i):
        v += pow(2,j)
    for j in range(i+1,30):
        if k&(1<<j) > 0:
            v += pow(2,j)
    kset.add(v)

kl = list(kset)
ans = 0
for ki in kl:
    v = 0
    for a,b in abl:
        if a > k: continue
        for i in range(30):
            if a&(1<<i) > 0 and ki&(1<<i) == 0:
                break
        else:
            v += b
    ans = max(ans, v)

print(ans)
