n=int(input())
pll=[]
for _ in range(n):
    p,l=map(int, input().split())
    pll.append((p,l))

dp={}
p,l=pll[0]
for i in range(-1000,1001):
    dp[i]=0
for i in range(-l,l+1):
    dp[i]=1

MOD=10**9+7
for i in range(1,n):
    prev_p,prev_l=pll[i-1]
    p,l=pll[i]
    new_dp={}
    cumsum={}
    cumsum[-1001]=0
    csum=0
    for j in range(-1000,1001):
        csum+=dp[j]
        csum%=MOD
        cumsum[j]=csum

    for j in range(-1000,1001):
        if abs(j)>l:new_dp[j]=0
        else:
            left=p+j
            maxr=left-prev_p-1
            if maxr>1000: maxr=1000
            # print(j,left,maxr)
            sums=cumsum[maxr]
            # print(sums)
            new_dp[j]=sums
    dp=new_dp.copy()

ans=0
p,l=pll[-1]
for k,v in dp.items():ans+=v
print(ans%MOD)