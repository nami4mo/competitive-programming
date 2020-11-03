from math import log2

n,m,d = map(int, input().split())
al = list(map(int, input().split()))
pos = list(range(n+1))

for a in al:
    pos[a],pos[a+1] = pos[a+1],pos[a]
    # print(pos)

dist = [0]*(n+1)
for i,p in enumerate(pos):
    dist[p] = i

# print(dist)

logk = int(log2(d))+1
db = [ [0]*(n+1) for _ in range(logk) ]
for ni in range(n+1): 
    db[0][ni] = dist[ni]

for ki in range(logk-1):
    for ni in range(n+1):
        db[ki+1][ni] = db[ki][db[ki][ni]]


for ni in range(1,n+1):
    now = ni
    for i in range(logk):
        if d&(1<<i) > 0:
            now = db[i][now]
    print(now)