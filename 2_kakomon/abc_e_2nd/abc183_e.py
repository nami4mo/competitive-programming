h,w=map(int, input().split())
sl=[list(input()) for _ in range(h)]

dp=[[0]*w for _ in range(h)]
dcsum={v:0 for v in range(-w,h+w+1)}
hcsum=[0]*w
wcsum=0

dp[0][0]=0
hcsum[0]=0
wcsum=0
MOD=10**9+7
for i in range(h):
    wcsum=0
    for j in range(w):
        if sl[i][j]=='#':
            wcsum=0
            hcsum[j]=0
            dcsum[i-j]=0
        else:
            if i==0 and j==0: dp[0][0]=1
            else: dp[i][j]=(wcsum+hcsum[j]+dcsum[i-j])%MOD
            wcsum+=dp[i][j]
            hcsum[j]+=dp[i][j]
            dcsum[i-j]+=dp[i][j]
            wcsum%=MOD
            hcsum[j]%=MOD
            dcsum[i-j]%=MOD
print(dp[-1][-1])
# print(dp)