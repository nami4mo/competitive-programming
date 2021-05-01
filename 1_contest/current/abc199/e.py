n,m=map(int, input().split())
dp=[0]*(1<<n)
xyzl=[[] for _ in range(n+1)]
for _ in range(m):
    x,y,z=map(int, input().split())
    y-=1
    xyzl[x].append((y,z))
    
dp[0]=1
lens=[[] for _ in range(n+1)]
for i in range(1<<n):
    x=bin(i).count("1")
    lens[x].append(i)
    yzl=xyzl[x]
    for y,z in yzl:
        cnt=0
        for j in range(n):
            if i&(1<<j) and j<=y:cnt+=1
        if cnt>z:
            dp[i]=-1
            break
    else:
        dp[i]=0

dp[0]=1
for i in range(1<<n):
    for j in range(n):
        if dp[i]==-1:continue
        if i&(1<<j): continue
        bits=i|(1<<j)
        if dp[bits]==-1:continue
        dp[bits]+=dp[i]
print(dp[-1])
