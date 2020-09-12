n,m = map(int, input().split())
scl = []
for _ in range(m):
    s,c = map(int, input().split())
    scl.append((s,c))

for i in range(0, 1000):
    si = str(i)
    if len(si) != n: continue
    for sc in scl:
        s,c = sc
        if si[s-1] != str(c):
            break
    else:
        print(i)
        exit()
else:
    print(-1)