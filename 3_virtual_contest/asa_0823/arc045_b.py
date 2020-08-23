n,m = map(int, input().split())
stl = []
for i in range(m):
    s,t = map(int, input().split())
    stl.append((s,t))

imos = [0]*(n+2)
for s,t in stl:
    imos[s] += 1
    imos[t+1] -= 1

clean_cnts = [0]*(n+1)
cnt = 0
for i in range(n+1):
    cnt += imos[i]
    clean_cnts[i] = cnt

clean_ont_cumsum = [0]*(n+1)
ccum = 0
for i in range(n+1):
    if clean_cnts[i] == 1:
        ccum += 1
    clean_ont_cumsum[i] = ccum

ansl = []
for i,(s,t) in enumerate(stl):
    if clean_ont_cumsum[t] - clean_ont_cumsum[s-1] == 0:
        ansl.append(i+1)

print(len(ansl))
for a in ansl: print(a)