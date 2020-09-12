n,m = map(int, input().split())
abl = []
cdl = []
for _ in range(n):
    a,b = map(int, input().split())
    abl.append((a,b))

for _ in range(m):
    c,d = map(int, input().split())
    cdl.append((c,d))


for a,b in abl:
    cmin = 10**10
    mini = -1
    for i,(c,d) in enumerate(cdl):
        v = abs(a-c)+abs(b-d)
        if v < cmin:
            cmin = v
            minc,mind = c,d
            mini = i+1
    print(mini) 