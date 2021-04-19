n,m,l=map(int, input().split())
INF=10**18
d=[[INF]*n for _ in range(n)]
for _ in range(m):
    a,b,c=map(int, input().split())
    a-=1
    b-=1
    d[a][b]=c
    d[b][a]=c


for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j],d[i][k] + d[k][j])

dd=[[INF]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if d[i][j]<=l:
            dd[i][j]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dd[i][j] = min(dd[i][j],dd[i][k] + dd[k][j])

al=[]
for _ in range(int(input())):
    s,t=map(int, input().split())
    s-=1
    t-=1
    ans=dd[s][t]-1
    if ans>=INF-1:ans=-1
    al.append(ans)

for a in al:print(a)