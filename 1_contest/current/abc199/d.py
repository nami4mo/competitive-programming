
n,m=map(int, input().split())
gl=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

dp=[[0]*3 for _ in range(n)]
vis=[False]*n
def dfs(node,pare):
    print(node)
    if vis[node]:return dp[node][0],dp[node][1],dp[node][2]
    cnts=[0]*3
    fg=False
    vis[node]=True
    for neib in gl[node]:
        if neib==pare:continue
        if vis[neib]:continue
        fg=True
        a,b,c=dfs(neib,node)
        cnts[0]+=a
        cnts[1]+=b
        cnts[2]+=c
    if not fg:
        for i in range(3):dp[node][i]=1
        return 1,1,1

    ans=[0]*3
    ans[0]=cnts[1]+cnts[2]
    ans[1]=cnts[2]+cnts[0]
    ans[2]=cnts[0]+cnts[1]
    dp[node]=ans[:]
    return ans[0],ans[1],ans[2]

ans=0
for i in range(n):
    if vis[i]:continue
    print('---',i)
    a,b,c=dfs(i,-1)
    ans+=(a+b+c)
print(dp)
print(ans)