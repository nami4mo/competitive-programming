h,w=map(int, input().split())
cl=[]
for _ in range(h):
    cl.append(list(input()))
al=[[0]*w for _ in range(h)]
for y in range(h):
    for x in range(w):
        if cl[y][x]=='+':al[y][x]=1
        else:al[y][x]=-1

INF=10**10
dp=[[INF]*w for _ in range(h)]

for y in range(h-1,-1,-1):
    for x in range(w-1,-1,-1):
        if y==h-1 and x==w-1:
            dp[y][x]=al[y][x]
            continue
        if y!=h-1 and x!=w-1:
            # print(y,x)
            ma=max(dp[y+1][x],dp[y][x+1])
            val=(-1)*ma+al[y][x]
            dp[y][x]=val
        elif y==h-1:
            val=(-1)*dp[y][x+1]+al[y][x]
            dp[y][x]=val
        elif x==w-1:
            val=(-1)*dp[y+1][x]+al[y][x]
            dp[y][x]=val

# print(dp)
dp[0][0]-=al[0][0]
ans=dp[0][0]
if ans<0:
    print('Takahashi')
elif ans>0:
    print('Aoki')
else:
    print('Draw')