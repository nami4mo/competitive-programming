n=int(input())
xyzl=[]
for _ in range(n):
    x,y,z=map(int, input().split())
    xyzl.append((x,y,z))

INF=10**18
dp=[[INF]*n for _ in range(1<<n)]
dp[1][0]=0
for i in range(1<<n):
    for j in range(n):
        if i&(1<<j)==0: continue
        for k in range(n):
            if i&(1<<k)>0: continue
            x,y,z=xyzl[j]
            x1,y1,z1=xyzl[k]
            dist=abs(x-x1)+abs(y-y1)+max(0,z1-z)
            dp[i|(1<<k)][k]=min(dp[i|(1<<k)][k], dp[i][j]+dist)
            # print(i,j,k)

ans=INF
for i in range(n):
    x,y,z=xyzl[i]
    x1,y1,z1=xyzl[0]
    dist=abs(x-x1)+abs(y-y1)+max(0,z1-z)
    ans=min(ans, dp[-1][i]+dist)
print(ans)
# print(dp)