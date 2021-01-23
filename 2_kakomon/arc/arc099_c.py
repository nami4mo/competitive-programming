n,m=map(int, input().split())
gll=[[True]*n for _ in range(n)]
for i in range(n):
    gll[i][i]=False
for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gll[a][b]=False
    gll[b][a]=False

gl=[[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if gll[i][j]:gl[i].append(j)

'''
各連結成分の二部グラフ判定（個数求め）
'''
from collections import deque
cntsl=[]
colors=[-1]*n # -1: no visit, 0: black, 1: white
for start in range(n):
    if colors[start]!=-1: continue
    q=deque([start])
    colors[start]=0
    cnts=[1,0]
    while q:
        poped=q.popleft()
        for neib in gl[poped]:
            if colors[neib]==-1:
                colors[neib]=colors[poped]^1
                cnts[colors[neib]]+=1
                q.append(neib)
            else:
                if colors[neib]==colors[poped]:
                    print(-1)
                    exit()
    cntsl.append(cnts)

# print(cntsl)
dp=[False]*(n+1)
dp[0]=True
for c1,c2 in cntsl:
    new_dp=[False]*(n+1)
    for i in range(n+1):
        if not dp[i]: continue
        # new_dp[i]=True
        if i+c1<=n: new_dp[i+c1]=True
        if i+c2<=n: new_dp[i+c2]=True
    dp=new_dp[:]

for i in range(n//2,-1,-1):
    if dp[i]:
        c1=i
        c2=n-i
        ans=c1*(c1-1)//2+c2*(c2-1)//2
        print(ans)
        break