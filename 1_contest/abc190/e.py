n,m=map(int, input().split())
gl=[ [] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

k=int(input())
cl=list(map(int, input().split()))
cl = [c-1 for c in cl]
ctoi={}
for i in range(k):
    ctoi[cl[i]]=i

INF=10**18
cdists=[]

from collections import deque
from itertools import combinations
for i,c in enumerate(cl):
    # print(c)
    q=deque([c])
    visited=[-1]*(n+1)
    visited[c]=0
    distcs=[]
    while q:
        poped=q.popleft()
        for neib in gl[poped]:
            if visited[neib]==-1:
                visited[neib]=visited[poped]+1
                q.append(neib)
    distcs=[INF]*k
    for c in cl:
        if visited[c]!=-1:
            distcs[ctoi[c]]=visited[c]
    cdists.append(distcs)


# INF = 10**9
# for _ in range(e):
#     s,t,d = map(int, input().split())
#     gl[s][t] = d

n=k
# print(n)
dp = [ [INF]*(n) for _ in range(2**n) ]
# dp[1][0] = 0
for i in range(n):
    # print(2**n,n)
    dp[2**i][i]=0

for i in range(2**n):
    for j in range(n):
        if dp[i][j] == INF: continue
        for k in range(n):
            if (i>>k)%2 == 1: continue

            dp[i|(1<<k)][k] = min(dp[i][j]+cdists[j][k], dp[i|(1<<k)][k])

ans=min(dp[-1])
if ans>=INF:
    ans=-2
print(ans+1)

# ans = INF
# for i in range(1,n): 
#     if gl[i][0] != INF:
#         ans = min(ans, dp[2**n-1][i] + gl[i][0])

# if ans == INF: ans = -1
# print(ans)