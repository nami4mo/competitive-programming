h,w,c=map(int, input().split())
al=[list(map(int, input().split())) for _ in range(h)]

INF=10**18
dp=[[INF]*w for _ in range(h)]
ans=INF
dp[0][0]=al[0][0]
for y in range(h):
    for x in range(w):
        if y+1<h:
            val=dp[y][x]+al[y+1][x]+c
            ans=min(ans,val)
            dp[y+1][x]=min(dp[y][x]+c, al[y+1][x], dp[y+1][x])
        if x+1<w:
            val=dp[y][x]+al[y][x+1]+c
            ans=min(ans,val)
            dp[y][x+1]=min(dp[y][x]+c, al[y][x+1], dp[y][x+1])
# print(ans)
# print(dp)
bl=[]
for row in al[::-1]:
    bl.append(row) 

INF=10**18
dp2=[[INF]*w for _ in range(h)]
ans2=INF
dp2[0][0]=bl[0][0]
for y in range(h):
    for x in range(w):
        if y+1<h:
            val=dp2[y][x]+bl[y+1][x]+c
            ans2=min(ans2,val)
            dp2[y+1][x]=min(dp2[y][x]+c, bl[y+1][x], dp2[y+1][x])
        if x+1<w:
            val=dp2[y][x]+bl[y][x+1]+c
            ans2=min(ans2,val)
            dp2[y][x+1]=min(dp2[y][x]+c, bl[y][x+1], dp2[y][x+1])
ans=min(ans,ans2)
print(ans)