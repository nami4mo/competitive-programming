
n,p,K=map(int, input().split())
al=[list(map(int, input().split())) for _ in range(n)]

def solve1(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    res=0
    for i in range(n):
        for j in range(i+1,n):
            if d[i][j]<=p:res+=1
    return res>=K

def solve2(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    res=0
    for i in range(n):
        for j in range(i+1,n):
            if d[i][j]<=p:res+=1
    return res<=K

def solve3(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    res=0
    for i in range(n):
        for j in range(i+1,n):
            if d[i][j]<=p:res+=1
    return res

INF=10**10
ok, ng = 1, INF+10000
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    d=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if al[i][j]==-1:d[i][j]=mid
            else:d[i][j]=al[i][j]
    res=solve1(d)
    if res: ok = mid
    else: ng = mid
right=ok

ok, ng = INF+10000, 0
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    d=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if al[i][j]==-1:d[i][j]=mid
            else:d[i][j]=al[i][j]
    res=solve2(d)
    if res: ok = mid
    else: ng = mid
left=ok

if right>=INF:
    d=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if al[i][j]==-1:d[i][j]=right
            else:d[i][j]=al[i][j]
    res1=solve3(d)
    if res1!=K:print(0)
    else:print('Infinity')
else:
    d=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if al[i][j]==-1:d[i][j]=right
            else:d[i][j]=al[i][j]
    res1=solve3(d)
    d=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if al[i][j]==-1:d[i][j]=left
            else:d[i][j]=al[i][j]
    res2=solve3(d)
    if res1!=K or res2!=K:print(0)
    else:print(max(0,right-left+1))
    # print(max(0,right-left+1))