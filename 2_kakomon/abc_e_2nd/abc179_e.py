from math import log2

n,x,m=map(int, input().split())
logn = int(log2(n))+1
db = [ [0]*m for _ in range(logn) ]
dbs = [ [0]*m for _ in range(logn) ]

for i in range(m):
    db[0][i]=(i**2)%m
    dbs[0][i]=(i**2)%m

for i in range(logn-1):
    for j in range(m):
        db[i+1][j]=db[i][db[i][j]]
        dbs[i+1][j]=dbs[i][db[i][j]]+dbs[i][j]

ans=x
now=x
for i in range(logn):
    if (n-1)&(1<<i) > 0:
        ans+=dbs[i][now]
        now=db[i][now]
print(ans)