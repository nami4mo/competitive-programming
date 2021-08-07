n=int(input())
al=list(map(int, input().split()))
INF=10**18
MAX=101
dp=[[INF]*MAX for _ in range(MAX)]
dp[0][0]=0

for i in range(n-2):
    new_dp=[[INF]*MAX for _ in range(MAX)] # dp[sum][last]
    for j in range(MAX): # prev_sum
        for k in range(j+1): # prev_last
            for l in range(MAX): # next_num
                if j+l>=MAX:break
                new_dp[j+l][l]=min(new_dp[j+l][l], dp[j][k]+(1+(k-l)**2)**0.5)
    dp=[[0]*MAX for _ in range(MAX)] # dp[sum][last]
    for j in range(MAX): # prev_sum
        for k in range(MAX): # prev_last
            dp[j][k]=new_dp[j][k]

ans=INF
asum=sum(al)
for i in range(MAX):
    d=dp[asum][i]+(1+(i-0)**2)**0.5
    ans=min(ans,d)
print(ans)