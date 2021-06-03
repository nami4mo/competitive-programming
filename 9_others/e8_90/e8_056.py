n,s=map(int, input().split())
abl=[]
for _ in range(n):
    a,b=map(int, input().split())
    abl.append((a,b))

dp=[[False]*(s+1) for _ in range(n+1)]
dp[0][0]=True

for i in range(n):
    a,b=abl[i]
    for j in range(s+1):
        if not dp[i][j]: continue
        if j+a<=s: dp[i+1][j+a]=True
        if j+b<=s: dp[i+1][j+b]=True

if not dp[n][s]:
    print('Impossible')
    exit()

ans=[]
curr=s
for i in range(n-1,-1,-1):
    a,b=abl[i]
    if curr-a>=0 and dp[i][curr-a]:
        ans.append('A')
        curr-=a
    elif curr-b>=0 and dp[i][curr-b]:
        ans.append('B')
        curr-=b

print(''.join(ans[::-1]))