from collections import deque
def make_order_parents(n,gl,root=0):
    order=[root]
    parents=[(-1,-1)]*n
    q=deque([root])
    while q:
        poped=q.popleft()
        for neib,w in gl[poped]:
            if parents[neib][0]!=-1 or neib==root:continue
            parents[neib]=(poped,w)
            order.append(neib)
            q.append(neib)
    return order,parents

n=int(input())
gl=[[] for _ in range(n)]
gli=[-1]*n
for i in range(n-1):
    u,v,w=map(int, input().split())
    u-=1
    v-=1
    gl[u].append((v,w))
    gl[v].append((u,w))

MAX=60
MOD=10**9+7
order,pare=make_order_parents(n,gl)
# print(pare)
dp0=[[0]*n for _ in range(MAX)]
dp1=[[0]*n for _ in range(MAX)]
for v in order[::-1]:
    if pare[v][0]==-1:continue
    parent,w=pare[v]
    for i in range(MAX):
        if w&(1<<i):
            dp0[i][parent]+=dp1[i][v]
            dp1[i][parent]+=(dp0[i][v]+1)
        else:
            dp0[i][parent]+=(dp0[i][v]+1)
            dp1[i][parent]+=dp1[i][v]

ans=0
q=deque([0])
used=[False]*n
used[0]=True

while q:
    poped=q.popleft()
    for neib,w in gl[poped]:
        if used[neib]:continue
        cnt=[0]*MAX
        for i in range(MAX):
            sum0=dp0[i][poped]
            sum1=dp1[i][poped]
            c0,c1=dp0[i][neib],dp1[i][neib]
            if w&(1<<i):
                c0,c1=c1,c0+1
            else:
                c0,c1=c0+1,c1
            cnt[i]+=c0*(sum1-c1)
            cnt[i]+=c1

        for i in range(MAX):
            ans+=cnt[i]*(1<<i)
            ans%=MOD
            # if i==MAX-1:
        q.append(neib)
        used[neib]=True

print(ans)

# print(dp0[:2])
# print(dp1[:2])
